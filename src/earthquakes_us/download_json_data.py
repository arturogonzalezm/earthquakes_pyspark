import os

import requests

root = os.path.dirname(__file__)
path = '../../data/all_month.geojson'
data = os.path.join(root, path)

url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'

print('-> Download started. . .')
r = requests.get(url)

with open(data, 'wb') as f:
    f.write(r.content)

# Retrieve HTTP meta-data
print("-> Status code: ", r.status_code)
print("-> Headers: ", r.headers['content-type'])
print("-> Encoding: ", r.encoding)
print("-> Download completed.")
