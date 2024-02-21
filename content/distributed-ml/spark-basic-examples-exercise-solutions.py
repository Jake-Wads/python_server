(weather
 .groupBy(year('date').alias('year'))
 .agg(sum('precipitation').alias('total_rain'))
 .sort('total_rain')
 .show())

(weather
 .groupBy(year('date').alias('year'))
 .agg(mean('wind').alias('avg_wind'))
 .sort('avg_wind')
 .show())

(weather
 .withColumn('month', month('date'))
 .filter(expr('month == 1'))
 .groupBy('weather')
 .count()
 .sort('count')
 .show())

(weather
 .withColumn('month', month('date'))
 .filter(expr('month == 7'))
 .filter(expr('weather == "sun"'))
 .filter(expr('year(date) IN (2013, 2014)'))
 .select(mean('temp_avg'))
 .show())

q32015weather = (weather
 .withColumn('quarter', quarter('date'))
 .filter(col('quarter') == 3)
 .groupBy('weather')
 .count())

total = q32015weather.agg(sum('count')).first()[0]

(q32015weather
 .withColumn('p', col('count') / total)
 .show())