## Advanced Pandas DataFrames

#### Think about Indexing/Subsetting as a Where clause in SQL

- Think of `mpg[mpg.hwy > 35]` as `select * from mpg where hwy > 35`
- Think of `mpg[mpg.hwy > 35].model` as `select model from mpg where hwy > 35`
- Think of `mpg[["hwy", "model"]]`  as `select hwy, model from mpg`

### Using Pandas to Read in Data and Create a Dataframe

`pd.read_csv("filename.csv")` reads in the contents of `filename.csv` as a dataframe	

`pd.read_json("filename.json")` reads in the json and transforms it to a dataframe

`pd.read_excel("filename.xlsx")`  reads the Excel spreadshsheet to a dataframe

`pd.read_clipboard()` pastes from your clipboard and *attempts* to generate a dataframe. Use this when you highlight and copy text or a table of data from some HTML.

`pd.read_sql(query, url)` takes in the `query` and `url` arguments as a strings. The `query` variable needs to be syntactically correct SQL and the `url` variable needs to be the `pymsql` string w/ connection details.

### Using  `pd.read_sql()`

1. First, create your `.gitignore` file and ensure it has a line for `env.py`. Add and commit your `.gitignore`
2. Create your `env.py` and assign 3 variables `host`, `user`, `password` to hold strings we used for MySQL.
3. Send in your syntactically correct MySQL as a Python string and the `url` string as inputs

```
from env import host, user, password
url = f'mysql+pymysql://{user}:{password}@{host}/employees'
query = 'SELECT * FROM employees LIMIT 5 OFFSET 50'
pd.read_sql(query, url)
```











### Using Group By to Aggregate

Group by returns a `groupby` object. To obtain data from the groupby object, we need to attach an aggregate function such as `count`, `mean`, `median`, `min`, `max`, or `agg`. 

````python
# The following code returns the average grade by each topic grouped by classroom
df.groupby("classroom").mean()
````

```python
# This returns the min, max, and average math grade because it's run on the column
df.groupby('classroom').math.agg(['min', 'mean', 'max'])
```

#### Using `.merge` to join dataframes together

Given a `roles` table with an `id`, and `name`, and a `users` table w/ the `role_id` foreign key,

`pd.merge(users, roles, left_on='role_id', right_on='id', how='left')`

### `.pipe` Pipelines

In the case when we have written multiple functions that accept a dataframe and return a dataframe, it's useful to use `.pipe` to compose them.

```python
# Example of sending a df through 2 functions that accept/return dataframes
df = some_function_that_returns_a_datatrame(
		another_function_accepting_returning_a_dataframe(df))
```

```python
# By piping the functions, we can read from left to right.
df = df.pipe(some_function_that_returns_a_datatrame)
       .pipe(another_function_accepting_returning_a_dataframe)
       .pipe(etc...)
```

