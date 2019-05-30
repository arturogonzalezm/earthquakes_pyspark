import os

from datetime import date
from constants import path_us


class CreateDailyFile:
    root = os.path.dirname(__file__)
    path = path_us
    file_name = "all_day-" + str(date.today().strftime('%d-%m-%Y')) + '.geojson'
    data = os.path.join(root, path, file_name)


class ReadDailyFile:
    root = os.path.dirname(__file__)
    path = path_us
    file_name = 'all_day-30-05-2019.geojson'
    data = os.path.join(root, path, file_name)
