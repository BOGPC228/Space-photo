import os
import json
from pathlib import Path
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

from download import download_img


def get_extension(urls):
    for url in urls:
        parse = urlparse(url)
        extension = (os.path.splitext(parse.path))[1]
    return extension


def fetch_nasa_last_launch(response, directory):
    urls = []
    nasa_json = response.json()
    search_key = 'url'
    for nasa in nasa_json:
        if search_key in nasa.keys():
            urls.append(nasa['url'])
    extension = get_extension(urls)
    for url_number, url in enumerate(urls):
        filename = f"nasax_{url_number}{extension}"
        file_path = os.path.join(directory, filename)
        download_img(url, file_path)


def main():
    load_dotenv()
    directory = "images"
    os.makedirs(directory, exist_ok=True)
    token = os.getenv("TOKEN_NASA")
    count_link = 50
    payload = {"count": count_link,
               "api_key": token}
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, payload)
    response.raise_for_status()
    fetch_nasa_last_launch(response, directory)

if __name__ == "__main__":
    main()
