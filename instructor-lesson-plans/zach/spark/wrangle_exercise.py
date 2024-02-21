# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Wrangle Exercises

# +
import pyspark
from pyspark.sql.functions import *

spark = pyspark.sql.SparkSession.builder.getOrCreate()
# -

# ## Data Prep

df = spark.read.csv('data/case.csv', header=True, inferSchema=True)
print('nrows:', df.count())
stray_animal_cases = df.filter(df.service_request_type == 'Stray Animal').count()
print('stray animal cases:', stray_animal_cases)

# +
# Rename column
df = df.withColumnRenamed('SLA_due_date', 'case_due_date')

# Convert to better data types
df = (
    df.withColumn('case_late', col('case_late') == 'YES')
    .withColumn('case_closed', col('case_closed') == 'YES')
)
df = df.withColumn('council_district', format_string('%04d', col('council_district')))
df = (
    df.withColumn('case_opened_date', to_timestamp(col('case_opened_date'), 'M/d/yy H:mm'))
    .withColumn('case_closed_date', to_timestamp(col('case_closed_date'), 'M/d/yy H:mm'))
    .withColumn('case_due_date', to_timestamp(col('case_due_date'), 'M/d/yy H:mm'))
)

# Cleanup text data
df = df.withColumn('request_address', lower(trim(col('request_address'))))
# Extract zipcode
df = df.withColumn('zipcode', regexp_extract(col('request_address'), r'\d+$', 0))

# Create a `case_lifetime` feature
df = (
    df.withColumn('case_age', datediff(current_timestamp(), 'case_opened_date'))
    .withColumn('days_to_closed', datediff('case_closed_date', 'case_opened_date'))
    .withColumn('case_lifetime', when(col('case_closed'), col('days_to_closed')).otherwise(col('case_age')))
    .drop('case_age', 'days_to_closed')
)

# Join departments and sources
depts = spark.read.csv('data/dept.csv', header=True, inferSchema=True)
sources = spark.read.csv('data/source.csv', header=True, inferSchema=True)

df = df.join(depts, 'dept_division', 'left').join(sources, 'source_id', 'left')

# # Train Test Split
# train, test = df.randomSplit([.8, .2], seed=123)
# train, validate, test = df.randomSplit([.7, .15, .15], seed=123)
# -

df.count()

df.count()

# In case we want to query our dataframe with Spark SQL:

df.createOrReplaceTempView('df')

# ## Initial Exploration Questions

# How old is the latest (in terms of days past SLA) currently open issue?
# How long has the oldest (in terms of days since opened) currently opened issue been open?
spark.sql('''
SELECT DATEDIFF(current_timestamp, case_due_date) AS days_past_due
FROM df
WHERE NOT case_closed
ORDER BY days_past_due DESC
LIMIT 15
''').show()

# How many Stray Animal cases are there?
df.filter(df.service_request_type == 'Stray Animal').count()

# 26760?

(
    df.groupBy('service_request_type')
    .count()
    .filter(expr('service_request_type == "Stray Animal"'))
    .show()
)

# How many service requests that are assigned to the Field Operations department (dept_division)
# are not classified as "Officer Standby" request type (service_request_type)?
(
    df.filter(df.dept_division == 'Field Operations')
    .filter(df.service_request_type != 'Officer Standby')
    .count()
)

# Another way to do it
(
    df.filter(expr("dept_division == 'Field Operations'"))
    .filter(expr('service_request_type != "Officer Standby"'))
    .count()
)

# +
# Convert the council_district column to a string column.

# Already done in the data prep
# -

# Extract the year from the case_closed_date column.
df.select('case_closed_date', year('case_closed_date')).show(5)

# Convert num_days_late from days to hours in new columns num_hours_late.
(
    df.withColumn('num_hours_late', df.num_days_late * 24)
    .select('num_days_late', 'num_hours_late')
    .show()
)

# +
# Join the case data with the source and department data.

# already joined in the data prep
# -

# Are there any cases that do not have a request source?
# are there any null values for source_id?
(
    df.select(df.source_id.isNull().cast('int').alias('is_null'))
    .agg(sum('is_null'))
    .show()
)

df.filter(col('source_id').isNull()).show(vertical=True)

# What are the top 10 service request types in terms of number of requests?
(
    df.groupby('service_request_type')
    .count()
    .sort(col('count').desc())
    .show(10, truncate=False)
)

# What are the top 10 service request types in terms of average days late?
# - just the late cases
# - for the late cases:
#   - what is the average number of days late by request type?
(
    df.where('case_late') # just the rows where case_late == true
    .groupBy('service_request_type')
    .agg(mean('num_days_late').alias('n_days_late'), count('*').alias('n_cases'))
    .sort(desc('n_days_late'))
    .show(10, truncate=False)
)

# Does number of days late depend on department?
(
    df.filter('case_late')
    .groupby('dept_name')
    .agg(mean('num_days_late').alias('days_late'), count('num_days_late').alias('n_cases_late'))
    .sort('days_late')
    .withColumn('days_late', round(col('days_late'), 1))
    .show(truncate=False)
)

df.groupby('dept_name').count().show(truncate=False)

# How do number of days late depend on department and request type?
(
    df.filter("case_closed")
    .filter("case_late")
    .groupby("standardized_dept_name", "service_request_type")
    .agg(avg("num_days_late").alias("days_late"), count("*").alias("n_cases"))
    .withColumn("days_late", round(col("days_late"), 1))
    .sort(desc("days_late"))
    .show(40, truncate=False)
)

# ## Handling Dates

# Quick Recap: getting data from spark dataframes:
#
# - `.show(n)`: prints the first `n` rows. Doesn't produce a value that can be used later
# - `.first`: gives us the first row object
# - `.head(n)`: gives us a list of the first `n` row objects
# - `.collect()`: turns *all* the rows into a list of row objects **be careful here**

df.select(max('case_opened_date')).collect()

max_date = df.select(max('case_opened_date'), max('case_closed_date')).first()[0]
max_date

# +
max_date = max_date.strftime('%Y-%m-%d %H:%M:%S')

df = (
    df.withColumn('case_age', datediff(lit(max_date), 'case_opened_date'))
    .withColumn('days_to_closed', datediff('case_closed_date', 'case_opened_date'))
    .withColumn('case_lifetime', when(col('case_closed'), col('days_to_closed')).otherwise(col('case_age')))
    .drop('case_age', 'days_to_closed')
)
# -

# ## Sidebar: Python Code Formatting

df = (df.withColumn('case_age', datediff(lit(max_date), 'case_opened_date')).withColumn('days_to_closed', datediff('case_closed_date', 'case_opened_date')).withColumn('case_lifetime', when(col('case_closed'), col('days_to_closed')).otherwise(col('case_age'))).drop('case_age', 'days_to_closed'))
