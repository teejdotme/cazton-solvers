from pyspark.sql import Row
from pyspark.sql import SparkSession
from pyspark.sql.functions import trim
from pyspark.sql import functions as F

def main():
    session = SparkSession.builder.appName("ghcnd-weather").getOrCreate()

    # load region metadata
    regions = session.read.text('hdfs://namenode:9000/workspace/data/ghcnd-states.txt')

    # name columns
    regions = regions.withColumn('CODE', regions[0].substr(0, 2))
    regions = regions.withColumn('NAME', regions[0].substr(F.lit(3), F.length(regions[0])))

    # alias regions
    regions = regions.alias('regions')

    # load station metadata
    stations = session.read.text('hdfs://namenode:9000/workspace/data/ghcnd-stations.txt')

    # name columns
    stations = stations.withColumn('ID', stations[0].substr(0, 11))
    stations = stations.withColumn('REGION', trim(stations[0].substr(39, 2)))

    # filter where region is non-empty
    stations = stations.filter("REGION != ''")

    # alias stations
    stations = stations.alias('stations')

    # load readings
    readings = session.read.csv('hdfs://namenode:9000/workspace/data/2019.csv')

    # name columns
    readings = readings.withColumn('STATION_ID', readings[0])
    readings = readings.withColumn('DATE', readings[1])
    readings = readings.withColumn('KEY', readings[2])
    readings = readings.withColumn('VALUE', readings[3].cast('float'))

    # filter to only min temp, max temp readings
    readings = readings.filter(readings['KEY'].isin(['TMIN', 'TMAX']))
    
    # sanity check on readings
    readings = readings.filter("VALUE <= 1500")
    readings = readings.filter("VALUE >= -1500")

    # migrate values to standard F
    readings = readings.withColumn('VALUE', F.round(((readings.VALUE / 10) * 9/5) + 32, 1))

    # alias readings
    readings = readings.alias('readings')

    # join readings to stations
    joined = readings.join(stations, readings.STATION_ID == stations.ID)

    # group joined data by region
    grouped = joined.groupBy('REGION')
    
    # calculate aggregates by region
    agged = grouped.agg(
        F.min('readings.VALUE').alias('MIN'),
        F.max('readings.VALUE').alias('MAX'),
        F.round(F.avg('readings.VALUE'), 1).alias('AVG'))

    # calculate variance by region
    agged = agged.withColumn('VARIANCE', F.round(agged.MAX - agged.MIN, 1))

    # join regions to the aggregates
    result = agged.join(regions, agged.REGION == regions.CODE)
    
    # select data and rename to final result columns
    result = result.select(
        F.col('regions.CODE').alias('STATE'), 
        F.col('regions.NAME').alias('NAME'),
        F.col('MIN').alias('MIN TEMP'),
        F.col('MAX').alias('MAX TEMP'), 
        F.col('AVG').alias('AVG TEMP'), 
        F.col('VARIANCE'))

    # sort final data by variance ascending
    result = result.sort(result.VARIANCE.asc())

    # output
    result \
        .write \
        .format('csv') \
        .mode('overwrite') \
        .option('header', False) \
        .option('sep', ',') \
        .save('hdfs://namenode:9000/workspace/output/report')
    
    # result.show()

main()