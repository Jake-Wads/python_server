import pyspark
import env

MYSQL_CONNECTOR_VERSION = '5.1.38'

DATABASE = 'a_database'
TABLE = 'some_db_table'

spark = (pyspark.sql.SparkSession.builder
 .config(f'spark.jars.packages', 'mysql:mysql-connector-java:{MYSQL_CONNECTOR_VERSION}')
 .getOrCreate())

df = (spark.read
 .option('driver', 'com.mysql.jdbc.Driver')
 .option('url', f'jdbc:mysql://{env.host}/{DATABASE}')
 .option('user', env.user)
 .option('password', env.password)
 .option('dbtable', TABLE)
 .format('jdbc')
 .load())