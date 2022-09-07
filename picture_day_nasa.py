import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

from download import download_img


def fetch_nasa_day_picture(token, directory, link_count=50):
    payload = {"count": link_count,
               "api_key": token}
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, payload)
    response.raise_for_status()
    nasa_pictures = response.json()
    for url_number, nasa_picture in enumerate(nasa_pictures):
        if 'url' not in nasa_picture.keys():
            continue
        parse = urlparse(nasa_picture['url'])
        extension = (os.path.splitext(parse.path))[1]
        filename = f"nasax_{url_number}{extension}"
        file_path = os.path.join(directory, filename)
        download_img(nasa_picture['url'], file_path)


def main():
    load_dotenv()
    directory = "images"
    os.makedirs(directory, exist_ok=True)
    token = os.getenv("NASA_TOKEN")
    fetch_nasa_day_picture(token, directory)


if __name__ == "__main__":
    main()
