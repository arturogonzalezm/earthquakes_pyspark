from pyspark.shell import sc
from pyspark.sql import HiveContext

from utils.utilities import ReadDailyFile

hc = HiveContext(sc)
sc.setLogLevel("INFO")


def get_place_and_magnitude():
    """
    :return: Magnitude and Places where magnitude is greater than 1.0
    """
    # Load JSON data
    json_data = hc.read.format("json").option("mode", "DROPMALFORMED").load(ReadDailyFile.data)
    # Create view earthquakes_us
    json_data.createOrReplaceTempView('earthquakes_us')
    # Query magnitude and places where magnitude is greater than 1.0
    earthquakes_df = hc.sql(
        "SELECT geometry.coordinates, geometry.type, properties.mag, properties.place "
        "FROM earthquakes_us "
        "WHERE properties.mag > 1.0")
    return earthquakes_df.show()
