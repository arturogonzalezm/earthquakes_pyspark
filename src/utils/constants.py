from datetime import date

url_us = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'
path_us = '../../data/'
file_name_us = "all_day-" + str(date.today().strftime('%d-%m-%Y')) + '.geojson'
