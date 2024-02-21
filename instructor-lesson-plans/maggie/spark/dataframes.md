## create dataframes

**Pandas**  

pd_df = pd.DataFrame({'col1': ['r1c1', 'r2c1', 'r3c1'], 'col2': ['r1c2', 'r2c2', 'r3c2']}, index = [1, 2, 3])
pd_df = pd.DataFrame([['r1c1', 'r1c2'], ['r2c1', 'r2c2'], ['r3c1', 'r3c2']], index = [1, 2, 3], columns = ['col1', 'col2'])

**PySpark**

sp_df = spark.createDataFrame(pd_df)

## Import data into dataframe

**Pandas**

pd.read_csv()
pd.read_json()
pd.read_excel()
pd.read_parquet()
pd.read_table()
pd.read_html()
pd.read_hdf()
pd.read_sql()
pd.read_clipboard()

**PySpark**

sp_df = spark.read.load("examples/src/main/resources/users.csv", format="csv", sep=":", inferSchema="true", header="true")
sp_df = spark.read.load("examples/src/main/resources/users.json", format="json") (read.json)
sp_df = spark.read.load("examples/src/main/resources/users.parquet") (parquet is default)
sp_df = spark.sql("SELECT * FROM parquet.`examples/src/main/resources/users.parquet`") 
spark.read.json("examples/src/main/resources/users.json")
spark.read.text("examples/src/main/resources/users.txt")


### manipulating columns

**Pandas**

remove columns: 
pd_df.drop(columns = ['c1', 'c2'])

rename columns: 
pd_df.rename(columns={"c1": "col1", "c2": "col2"})

add columns:
pd_df.assign(area = pd_df.length * pd_df.width)
pd_df['area'] = pd_df.length * pd_df.width


**PySpark**
remove columns:
sp_df.drop("c1", "c2")
sp_df.drop(sp_df.c1).drop(sp_df.c2)

rename columns:
sp_df.withColumnRenamed('col1', 'c1')

add columns:
sp_df.withColumn("area", expr("length * width"))
sp_df.withColumn("area", col("length") * col("width"))

avg_column = (col("hwy") + col("cty")) / 2

mpg.select(
    col("hwy").alias("highway_mileage"),
    mpg.cty.alias("city_mileage"),
    avg_column.alias("avg_mileage"),
).show(5)


querying/subsetting

**Pandas**

**PySpark**
from pyspark.sql import functions as F
sp_df.select()

sp_df.col1.isin()
sp_df.col

grouping & aggregating

**Pandas**
pd_df.groupby(['c1']).count()
pd_df.groupby(['c1']).agg('c2': ['sum', 'min'], 'c3': ['mean', 'max'])
pd_df.groupby(['c1']).agg(['sum', 'min', 'mean', 'max'])

**PySpark**
sp_df.groupBy('c1').count()
sp_df.groupBy('c1').agg({"c2": "max"}).collect()
from pyspark.sql import functions as F
sp_df.groupBy('c1').agg(F.min(sp_df.c2)).collect()

mpg.select(
    sum(mpg.hwy) / count(mpg.hwy).alias("average_1"),
    avg(mpg.hwy).alias("average_2"),
    min(mpg.hwy),
    max(mpg.hwy),
).show()

concatenate column values: str(pd_df.c1) + str(pd_df.c2) |  sp_df.select(concat(sp_df.c1, sp_df.c2))

### missing values

**Pandas**
pd_df.dropna()
pd_df.fillna(value = 0)

**PySpark**
sp_df.na.drop()
sp_df.na.fill(0)


writing dataframes

convert datatypes: 
pd_df.c1.astype("int"), pd_df.c1.astype("float"), pd_df.to_numeric(pd_df.c1), pd_df.to_datetime(pd_df.c2) | 
sp_df.select(sp_df.c1.cast("string"))

summarize

describe the index: pd_df.index
rows x columns: pd_df.shape
return the column names: pd_df.columns
column names, count, non-null counts, datatypes: 
number of non-null values: pd_df.count()
return df column names and data types:  sp_df.dtypes
return the schema of df: pd_df.info() | sp_df.schema, sp_df.printSchema()
compute summary statistics: pd_df.describe()   |   sp_df.describe().show()
return the column names: sp_df.columns
count the number of rows: len(pd_df), sp_df.count()
count the number of distinct rows: len(df.drop_duplicates()) |  sp_df.distinct().count()
print the logical and physical plans: sp_df.explain()

subset rows: 

return the first 5 rows: pd_df.head()  |  sp_df.show(5), sp_df.head(5), sp_df.take(5)
return the first 20 rows: pd_df.head(20)  |  sp_df.show(), sp_df.head(), sp_df.take() 
return the first row: pd_df.head(1)  | sp_df.first()
return the last n rows: pd_df.tail()  |
return a random sample of rows: pd_df.sample(frac = 0.5), pd_df.sample(n = 10)
return rows by position: pd_df.iloc[10:20] |  
select and order the top n entries: pd_df.nlargest(n, 'c1')
select and order the bottom n entries: pd_df.nsmallest(n, 'c1')

filter: pd_df[pd_df.c1 > 0]  |  sp_df.filter(df['c1'] > 0), sp_df.where(df['c1'] == )

Spark provides two dataframe methods, .filter and .where, which both allow us to select a subset of the rows of our dataframe.

mpg.filter(mpg.cyl == 4).where(mpg["class"] == "subcompact").show()


Similar to an IF in Excel, CASE...WHEN in SQL, or np.where in python, spark provides a when function.

The when function lets us specify a condition, and a value to produce if that condition is true:

from pyspark.sql.functions import when
mpg.select(mpg.hwy, when(mpg.hwy > 25, "good_mileage").alias("mpg_desc")).show(
    12
)


subset columns: 
select multiple columns: pd_df[['c1', 'c2']]  |  sp_df.select("c1", "c2")
select one column: pd_df['c1'], pd_df.c1, df.loc[:, 'c1']
select columns whose name matches regular expression: pd_df.filter(regex = '\_scaled')
select all columns between c1 and c3 (inclusive): pd_df.loc[:,'c1':'c3'] | 
select columns in positions 0 & 2: pd_df.iloc[:,[0,2]]
select rows meeting a logical condition, and only specified columns: pd_df.loc[pd_df['c1'] > 0, ['c1','c3']]

set values: 
set values for an entire column: pd_df.loc[:, 'c3'] = 30 | 
set values for an entire row: pd_df.loc['r1'] = 10 | 
Set value for all items matching the list of labels: df.loc[['r1', 'r3'], ['c2']] = 50

combining datasets

**Pandas**

**PySpark**


plotting

**Pandas**

**PySpark**



pd_df.col1: Series of values from pd_df  |  sp_df.col1: a Column object, which is an object that represents a vertical slice of a dataframe, but does not contain the data itself.

regex

The regexp_extract function lets us specify a regular expression with at least one capture group, and create a new column based on the contents of a capture group.

textdf.select(
    "address",
    regexp_extract("address", r"^(\d+)", 1).alias("street_no"),
    regexp_extract("address", r"^\d+\s([\w\s]+?),", 1).alias("street"),
).show(truncate=False)


regexp_replace lets us make substitutions based on a regular expression.

textdf.select(
    "address",
    regexp_replace("address", r"^.*?,\s*", "").alias("city_state_zip"),
).show(truncate=False)



