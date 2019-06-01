from earthquakes_us.extract_json_data import download_json_file
from earthquakes_us.process_json_data import transform_load


def main():
    """
    :return: ETL/ELT
    """
    download_json_file()
    transform_load()


if __name__ == '__main__':
    main()
