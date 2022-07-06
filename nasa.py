import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

from download import download_img


def fetch_nasa_picture_day(token, directory, count_link=50):
    payload = {"count": count_link,
               "api_key": token}
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, payload)
    response.raise_for_status()
    nasa_json = response.json()
    for url_number, nasa in enumerate(nasa_json):
        if 'url' in nasa.keys():
            parse = urlparse(nasa['url'])
            extension = (os.path.splitext(parse.path))[1]
            filename = f"nasax_{url_number}{extension}"
            file_path = os.path.join(directory, filename)
            download_img(nasa['url'], file_path)


def main():
    load_dotenv()
    directory = "images"
    os.makedirs(directory, exist_ok=True)
    token = os.getenv("NASA_TOKEN")
    fetch_nasa_picture_day(token, directory)


if __name__ == "__main__":
    main()
