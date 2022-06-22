import os
import json
from pathlib import Path

import requests

from download import download_img


def fetch_spacex_last_launch(directory):
    url = "https://api.spacexdata.com/v3/launches"
    response = requests.get(url)
    response.raise_for_status()
    start_spacex_all = response.json()
    for spacex_one in start_spacex_all:
        if spacex_one['links']['flickr_images']:
            spacex_link = spacex_one['links']['flickr_images']
            break
    for url_number, url in enumerate(spacex_link):
        filename = 'spacex'
        file_path = f'{directory}/{filename}{url_number}.jpg'
        download_img(url, file_path)


def main():
    directory = "images"
    os.makedirs(directory, exist_ok=True)
    fetch_spacex_last_launch(directory)


if __name__ == "__main__":
    main()
