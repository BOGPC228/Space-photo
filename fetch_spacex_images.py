import os
from urllib.parse import urlparse

import requests

from download import download_img


def fetch_spacex_last_launch(directory):
    url = "https://api.spacexdata.com/v3/launches"
    response = requests.get(url)
    response.raise_for_status()
    start_all_spacex = response.json()
    for start_one_spacex in start_all_spacex:
        if start_one_spacex['links']['flickr_images']:
            spacex_link = start_one_spacex['links']['flickr_images']
            break
    for url_number, url in enumerate(spacex_link):
        parse = urlparse(url)
        extension = (os.path.splitext(parse.path))[1]
        filename = f'spacex_{url_number}{extension}'
        file_path = os.path.join(directory, filename)
        download_img(url, file_path)


def main():
    directory = "images"
    os.makedirs(directory, exist_ok=True)
    fetch_spacex_last_launch(directory)


if __name__ == "__main__":
    main()
