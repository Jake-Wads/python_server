% Data Wrangling with Spark

## Intro

Create the spark session object

- this could be very complicated, but might be documented
- data location might also be pretty complicated
- difference is in setup / configuration, spark dataframe api code we write
  here is the same as what you would write connected to a 100 node cluster

## Reading/Writing data

- Spark can read json, parquet, jdbc in several ways that produce the same
  result
- `spark.read.csv("data/source.csv", header=True, inferSchema=True)`

### Data Schemas

- Goal is exposure here, there is no exercise for this
- `schema=` instead of `inferSchema`
- speed up processing
- ensure data integrity
- list of common types in the curriculum

```python
from pyspark.sql.types import StructType, StructField, StringType

schema = StructType([
    StructField("source_id", StringType()),
    StructField("source_username", StringType()),
])

spark.read.csv("data/source.csv", header=True, schema=schema)
```

### Writing data

- json, csv, parquet, jdbc
- `df.write.json`

## Data Prep

1. Read `case.csv`
1. Rename `SLA_due_date` -> `case_due_date` with `.withColumnRenamed`
1. Convert `case_closed` and `case_late` into booleans
1. Convert `council_district` to a string type and pad with `0`s
    - `col(...).cast("string")`
    - or in one operation: `format_string("%03d", col(...))`
1. Convert `case_opened_date`, `case_closed_date`, and `case_due_date` to dates
    - with `to_timestamp`
    - java `SimpleDateFormat`
    - `M/d/yy H:mm`
1. Trim + lowercase `request_address`
1. Days late to weeks late
1. Extract `zipcode` from address
1. New features
    - `case_age`: `datediff(current_timestamp(), "case_opened_date")`
    - `days_to_closed`: date diff of case_closed - case_opened
    - `case_lifetime`: `days_to_closed` when the case is cloed else
      `case_age`
1. Join department data `.join(dept, "dept_division", "left")`
    - duplicated column names after the join, drop everything but
      `dept_division` using `df.column_name` to disambiguate
1. Data Splitting: `train, test = df.randomSplit([.8, .2])`
