from earthquakes_us.transform_json_data import get_place_and_magnitude
from earthquakes_us.extract_json_data import download_data


def main():
    # Extract
    download_data()
    # Transform
    get_place_and_magnitude()
    # Load


if __name__ == '__main__':
    main()
