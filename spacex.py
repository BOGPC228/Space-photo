import os
import json
from pathlib import Path
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


path = "images"
os.makedirs(path, exist_ok=True)


def get_extension(urls):
    for url in urls:
        parse = urlparse(url)
        extension = (os.path.splitext(parse.path))[1]
    return extension


def download_img(extension, url_number, url, path):
    filename = f"nasax_{url_number}.{extension}"
    file_path = os.path.join(path, filename)
    response = requests.get(url)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(download_img, response):
    urls = []
    nasa_json = response.json()
    search_key = 'url'
    for nasa in nasa_json:
        if search_key in nasa.keys():
            print("В словаре есть ключ")
            urls.append(nasa['url'])
        else:
            print("В словаре нет ключа")
    extension = get_extension(urls)
    for url_number, url in enumerate(urls, 1):
        download_img(extension, url_number, url, path)


def main():
    load_dotenv()
    token = os.getenv("TOKEN_NASA")
    count_link = 50
    payload = {"count": count_link,
               "api_key": token}
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, payload)
    response.raise_for_status()
    fetch_spacex_last_launch(download_img, response)


if __name__ == "__main__":
    main()
