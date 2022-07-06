import os
import datetime

import requests
from dotenv import load_dotenv

from download import download_img


def generation_number_link(response, payload, directory):
    epic_link = response.json()
    for url_number, link in enumerate(epic_link):
        link_name = link['image']
        image_date = link['date']
        date_t = datetime.datetime.fromisoformat(image_date)
        date_format = date_t.strftime("%Y/%m/%d")
        link_template = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png'
        link_template = link_template.format(date_format, link_name)
        filename = f"epic_{url_number}.png"
        file_path = os.path.join(directory, filename)
        download_img(link_template, file_path, payload)


def main():
    load_dotenv()
    directory = "images"
    os.makedirs(directory, exist_ok=True)
    token = os.getenv("NASA_TOKEN")
    payload = {"api_key": token}
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, payload)
    response.raise_for_status()
    generation_number_link(response, payload, directory)


if __name__ == "__main__":
    main()
