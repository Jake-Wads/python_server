## Reading From a MySQL Database


```python
import pyspark
import env
```


```python
MYSQL_CONNECTOR_VERSION = '8.0.16'

spark = (pyspark.sql.SparkSession.builder
 .config('spark.jars.packages', f'mysql:mysql-connector-java:{MYSQL_CONNECTOR_VERSION}')
 .getOrCreate())
```

## Read a Table


```python
db = 'employees'
table = 'salaries'

df = (spark.read
 .option('driver', 'com.mysql.jdbc.Driver')
 .option('url', f'jdbc:mysql://{env.host}/{db}')
 .option('user', env.user)
 .option('password', env.password)
 .option('dbtable', table)
 .format('jdbc')
 .load())
```


```python
df.show()
```

    +------+------+----------+----------+
    |emp_no|salary| from_date|   to_date|
    +------+------+----------+----------+
    | 10001| 60117|1986-06-25|1987-06-25|
    | 10001| 62102|1987-06-25|1988-06-24|
    | 10001| 66074|1988-06-24|1989-06-24|
    | 10001| 66596|1989-06-24|1990-06-24|
    | 10001| 66961|1990-06-24|1991-06-24|
    | 10001| 71046|1991-06-24|1992-06-23|
    | 10001| 74333|1992-06-23|1993-06-23|
    | 10001| 75286|1993-06-23|1994-06-23|
    | 10001| 75994|1994-06-23|1995-06-23|
    | 10001| 76884|1995-06-23|1996-06-22|
    | 10001| 80013|1996-06-22|1997-06-22|
    | 10001| 81025|1997-06-22|1998-06-22|
    | 10001| 81097|1998-06-22|1999-06-22|
    | 10001| 84917|1999-06-22|2000-06-21|
    | 10001| 85112|2000-06-21|2001-06-21|
    | 10001| 85097|2001-06-21|2002-06-21|
    | 10001| 88958|2002-06-21|9998-12-31|
    | 10002| 65828|1996-08-02|1997-08-02|
    | 10002| 65909|1997-08-02|1998-08-02|
    | 10002| 67534|1998-08-02|1999-08-02|
    +------+------+----------+----------+
    only showing top 20 rows




```python
from pyspark.sql.functions import avg

df.agg(avg('salary')).show()
```

    +------------------+
    |       avg(salary)|
    +------------------+
    |63810.744836143705|
    +------------------+




```python
df.cache().count()
```




    2844047


## Read a Query


```python
(spark.read
 .option('driver', 'com.mysql.jdbc.Driver')
 .option('url', f'jdbc:mysql://{env.host}/{db}')
 .option('user', env.user)
 .option('password', env.password)
 .option('query', 'SELECT * FROM departments')
 .format('jdbc')
 .load()).show()
```

    +-------+------------------+
    |dept_no|         dept_name|
    +-------+------------------+
    |   d009|  Customer Service|
    |   d005|       Development|
    |   d002|           Finance|
    |   d003|   Human Resources|
    |   d001|         Marketing|
    |   d004|        Production|
    |   d006|Quality Management|
    |   d008|          Research|
    |   d007|             Sales|
    +-------+------------------+


