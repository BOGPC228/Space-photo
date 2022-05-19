import os
from pathlib import Path

import requests


file_path = "images_n"
os.makedirs(file_path, exist_ok=True)


url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
filename = "nasa.png"
path = f"{file_path}/{filename}"


def image_url(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)
    file.close()
    print(url)
image_url(url, path)
