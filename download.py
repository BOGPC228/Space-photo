import requests


def download_img(url, file_path, payload=None):
    response = requests.get(url, payload)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)
