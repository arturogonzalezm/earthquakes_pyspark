import os

from utils.constants import path_us, file_name_us


class CreateReadDailyFile:
    root = os.path.dirname(__file__)
    path = path_us
    file_name = file_name_us
    data = os.path.join(root, path, file_name)
