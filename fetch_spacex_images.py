import os
import json
from pathlib import Path

import requests

from download import download_img


def fetch_spacex_last_launch(response, directory):
    spacex = response.json()
    for spacee in spacex:
        if spacee['links']['flickr_images']:
            sapce = spacee['links']['flickr_images']
    for url_number, url in enumerate(sapce):
        filename = 'spacex'
        file_path = f'{directory}/{filename}{url_number}.jpg'
        download_img(url, file_path)


def main():
    directory = "images"
    os.makedirs(directory, exist_ok=True)
    url = "https://api.spacexdata.com/v3/launches"
    response = requests.get(url)
    response.raise_for_status()
    fetch_spacex_last_launch(response, directory)


if __name__ == "__main__":
    main()
