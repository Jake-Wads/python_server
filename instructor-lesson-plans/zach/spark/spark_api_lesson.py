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

# # Spark API

# +
import pyspark

spark = pyspark.sql.SparkSession.builder.getOrCreate()
# -

spark

# For demonstration, we'll create a spark dataframe from a pandas dataframe.

import numpy as np
import pandas as pd
import pydataset

tips = pydataset.data('tips')
df = spark.createDataFrame(tips)
df.show()

# ## DataFrame Basics

df.show(5)

df.head(5)

# Don't do this!
# just use .show to view df contents
df2 = df.show(10)

type(df2)

# ### Selecting Columns

df.select('total_bill', 'tip', 'size', 'day').show()

df.select('*')

df.select(df.tip / df.total_bill).show(5)

col = df.tip / df.total_bill
col

df.select('*', col.alias('tip_pct')).show(5)

df_with_tip_pct = df.select('*', col.alias('tip_pct'))

df_with_tip_pct.show(5)

# ### Selecting w/ Built In Functions

from pyspark.sql.functions import sum, mean, concat, lit, regexp_extract, regexp_replace, when

df.select(mean(df.tip), sum(df.total_bill)).show()

df.select(concat('day', lit(' '), 'time')).show(5)

df.select(df.time.cast('int')).show(5)

df = df.select(
    '*',
    (df.tip / df.total_bill).alias('tip_pct')
)

# ### When / Otherwise

df.select(
    'tip_pct',
    (when(df.tip_pct > .2, 'good tip')
     .otherwise('not good tip')
     .alias('tip_desc'))
).show(25)

# ### Regex

df.select(
    'time',
    regexp_extract('time', r'(\w).*', 1).alias('first_letter'),
    regexp_replace('time', r'[aeiou]', 'X')
).show(5)

# ## Transforming Rows

df.show()

# ### Sorting

df.orderBy(df.total_bill).show()

df.sort(df.day, df.size).show()

from pyspark.sql.functions import asc, desc, col

df.sort(df.day, asc('time'), desc('size')).show()

col('size').asc()

df.sort(col('size').desc(), col('time')).show()

# ### Filtering

df.where(df.tip < 4).show()

mask = df.tip < 4
df.where(mask).show()

df.filter((df.time == "Dinner") | (df.tip <= 2)).sort('tip').show()

df.where(df.smoker == "Yes").where(df.day == "Sat").show()

# ## Aggregating

from pyspark.sql.functions import mean, min, max

df.show(5)

df.groupBy('time').agg(mean('tip')).show()

df.groupBy('time').agg(min('tip'), mean('tip'), max('tip')).show()

df.groupBy('time').agg(mean('tip').alias('avg_tip')).show()

df.groupBy('time', 'day').agg(mean('total_bill')).show()

df.crosstab('time', 'day').show()

df.groupBy('time').pivot('day').agg(mean('total_bill')).show()

# `.crosstab` is just for counts, for other methods of summarizing groups, use `.groupBy` (maybe in combination with `.pivot`) + `.agg`.

# ## Additional Features

# ### Spark SQL

df.createOrReplaceTempView('tips')

spark.sql('''
SELECT *
FROM tips
''').show()

# find the tip, total_bill, and day with the highest overall sales for that day
spark.sql('''
SELECT tip, total_bill, day
FROM tips
WHERE day = (
    SELECT day
    FROM tips
    GROUP BY day
    ORDER BY sum(total_bill) DESC
    LIMIT 1
)    
''').show()

# ### More Spark Dataframe Manipulation

df.where(
    df.time == 'Dinner'
).select(
    '*',
    (df.tip / df.total_bill).alias('tip_pct'),
).explain()

df.select(
    '*',
    (df.tip / df.total_bill).alias('tip_pct'),
).where(
    df.time == 'Dinner'
).explain()

# ### Mixing in SQL Expressions

from pyspark.sql.functions import expr

# Expr lets us mix in parts of SQL into our dataframes

df.select(
    '*',
    expr('tip / total_bill as tip_pct')
).where(
    expr('day = "Sun" AND time = "Dinner"')
).show()

# ## Joins

df1 = spark.createDataFrame(pd.DataFrame({
    'id': np.arange(100) + 1,
    'x': np.random.randn(100).round(3),
    'group_id': np.random.choice(range(1, 7), 100),
}))
df2 = spark.createDataFrame(pd.DataFrame({
    'id': range(1, 7),
    'group': list('abcdef')
}))
df1.show(5)
df2.show()

df_merged = df1.join(df2, df1.group_id == df2.id)
df_merged.show(5)

df1.join(df2.withColumnRenamed('id', 'group_id'), 'group_id').show(5)
