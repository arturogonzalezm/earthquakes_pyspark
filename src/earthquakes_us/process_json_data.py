from pyspark.shell import sc
from pyspark.sql import HiveContext

from utilities import CreateReadDailyFile

hc = HiveContext(sc)
sc.setLogLevel("INFO")


def transform_load():
    read_daily_file = CreateReadDailyFile()
    json_data = hc.read.format("json").option("mode", "DROPMALFORMED").load(read_daily_file.data)
    # Create view earthquakes_us
    json_data.createOrReplaceTempView('earthquakes_us_historical')
    # Query magnitude and places where magnitude is greater than 1.0
    earthquakes_df = hc.sql(
        "SELECT id, geometry.type as shape_type, geometry.coordinates, properties.mag, properties.place "
        "FROM earthquakes_us_historical "
        "WHERE properties.mag > 1.0")

    earthquakes_df.write.format('jdbc').options(
        url='jdbc:postgresql://localhost:5432/earthquakes',
        driver='org.postgresql.Driver',
        dbtable='earthquakes_daily_historical').mode('append').save()
