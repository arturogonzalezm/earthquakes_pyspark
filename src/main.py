from earthquakes_us.transform_json_data import get_place_and_magnitude
from earthquakes_us.extract_json_data import download_data


def main():
    download_data()
    get_place_and_magnitude()


if __name__ == '__main__':
    main()
