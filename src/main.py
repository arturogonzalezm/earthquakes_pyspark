import os

from pyspark.shell import sc

from pyspark.sql import HiveContext

root = os.path.dirname(__file__)
path = '../data/all_month.geojson'
data = os.path.join(root, path)

hc = HiveContext(sc)


def get_place_and_magnitude():
    json_data = hc.read.format("json").option("mode", "DROPMALFORMED").load(data)
    json_data.createOrReplaceTempView('earthquakes_us')
    # json_data.write.format("orc").saveAsTable("earthquakes_us")
    earthquakes_df = hc.sql("SELECT properties.mag, properties.place "
                            "FROM earthquakes_us "
                            "WHERE properties.mag > 1.0")
    earthquakes_df.show()


def main():
    get_place_and_magnitude()


if __name__ == '__main__':
    main()
