import os

from constants import path_us, file_name_us


class CreateDailyFile:
    root = os.path.dirname(__file__)
    path = path_us
    file_name = file_name_us
    data = os.path.join(root, path, file_name)


class ReadDailyFile:
    root = os.path.dirname(__file__)
    path = path_us
    # file_name = 'all_day-30-05-2019.geojson'
    file_name = file_name_us
    data = os.path.join(root, path, file_name)
