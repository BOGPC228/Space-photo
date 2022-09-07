import os
import datetime

import requests
from dotenv import load_dotenv

from download import download_img


def get_epic_images(response, payload, directory):
    for url_number, link in enumerate(response.json()):
        link_name = link['image']
        date_format = format_date(link)
        link_template = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/{}{}'
        finished_link = link_template.format(date_format, link_name, '.png')
        filename = f"epic_{url_number}.png"
        file_path = os.path.join(directory, filename)
        download_img(finished_link, file_path, payload)


def format_date(link):
    image_date = link['date']
    date_time = datetime.datetime.fromisoformat(image_date)
    date_format = date_time.strftime("%Y/%m/%d")
    return date_format


def main():
    load_dotenv()
    directory = "images"
    os.makedirs(directory, exist_ok=True)
    token = os.getenv("NASA_TOKEN")
    payload = {"api_key": token}
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, payload)
    response.raise_for_status()
    get_epic_images(response, payload, directory)


if __name__ == "__main__":
    main()

