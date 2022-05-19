import os
import json
import datetime
from pathlib import Path
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

path = "images_epic"
os.makedirs(path, exist_ok=True)


def download_img(path, payload, url_end, url_number):
    filename = f"epic_{url_number}.png"
    file_path = os.path.join(path, filename)
    response = requests.get(url_end, payload)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)


def get_date_and_title(response):
    image_name = []
    date = []
    epic_json = response.json()
    image_key = 'image'
    date_key = 'date'
    for epic in epic_json:
        if image_key and date_key in epic.keys():
            image_name.append(epic['image'])
            date.append(epic['date'])
        else:
            continue
    return image_name, date


def sorted_date_and_image(date, image_name):
    for time in date:
        date_sorted = time
    for img in image_name:
        image_sorted = img
    return date_sorted, image_sorted


def assembly_sorted_time(date_sorted):
    date_t = datetime.datetime.fromisoformat(date_sorted)
    date_format = date_t.strftime("%Y/%m/%d/%H/%M/%S")[:-9]
    return date_format


def generation_number_link(date_format, response, payload):
    link_epic = response.json()
    for url_number, link in enumerate(link_epic, 1):
        link_name = link['image']
        url_end = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png'
        url_end = url_end.format(date_format, link_name)
        download_img(path, payload, url_end, url_number)


def main():
    load_dotenv()
    token = os.getenv("TOKEN_NASA")
    payload = {"api_key": token}
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, payload)
    response.raise_for_status()
    image_name, date = get_date_and_title(response)
    date_sorted, image_sorted = sorted_date_and_image(date, image_name)
    date_format = assembly_sorted_time(date_sorted)
    generation_number_link(date_format, response, payload)


if __name__ == "__main__":
    main()
