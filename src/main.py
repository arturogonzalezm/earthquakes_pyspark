import os

from pyspark.shell import sc

from pyspark.sql import HiveContext

root = os.path.dirname(__file__)
path = '../data/all_month.geojson'
data = os.path.join(root, path)

hc = HiveContext(sc)
sc.setLogLevel("INFO")


def get_place_and_magnitude():
    """
    :return: Magnitude and Places where magnitude is greater than 1.0
    """
    # Load JSON data
    json_data = hc.read.format("json").option("mode", "DROPMALFORMED").load(data)
    # Create view earthquakes_us
    json_data.createOrReplaceTempView('earthquakes_us')
    # Query magnitude and places where magnitude is greater than 1.0
    earthquakes_df = hc.sql("SELECT properties.mag, properties.place "
                            "FROM earthquakes_us "
                            "WHERE properties.mag > 1.0")
    earthquakes_df.show()


def main():
    """
    :return: Calling magnitude and places where magnitude is greater than 1.0 function
    """
    get_place_and_magnitude()


if __name__ == '__main__':
    main()
