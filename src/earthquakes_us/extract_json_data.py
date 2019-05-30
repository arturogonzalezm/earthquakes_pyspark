import requests

from constants import url_us
from utils import CreateDailyFile


def download_data():
    print('-> Download started. . .')
    r = requests.get(url_us)

    with open(CreateDailyFile.data, 'wb') as f:
        f.write(r.content)

    # Retrieve HTTP meta-data
    print("-> Status code: ", r.status_code)
    print("-> Headers: ", r.headers['content-type'])
    print("-> Encoding: ", r.encoding)
    print("-> Download completed.")
