import requests

from utils.constants import url_us
from utils.utilities import CreateReadDailyFile


def download_json_file():
    """
    :return: Extract a JSON file on daily basis.
    """
    print('-> Download started. . .')
    r = requests.get(url_us)
    create_daily_file = CreateReadDailyFile()
    with open(create_daily_file.data, 'wb') as f:
        f.write(r.content)

    # Retrieve HTTP meta-data
    print("-> Status code: ", r.status_code)
    print("-> Headers: ", r.headers['content-type'])
    print("-> Encoding: ", r.encoding)
    print("-> Download completed.")
