import os
import requests
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime
from filemane_extension import get_filename_extension


def get_nasa_picture_urls(token_api_nasa):
    nasa_api_url = "https://api.nasa.gov/planetary/apod"
    params = {
        "start_date": "2021-10-01",
        "end_date": "2021-11-01",
        "api_key": token_api_nasa
    }
    response = requests.get(nasa_api_url, params=params)
    response.raise_for_status()
    urls = [url.get("hdurl") for url in response.json()]
    photo_urls = [url for url in urls if url]

    return photo_urls


def get_nasa_epic_urls(token_api_nasa):
    nasa_api_epic_url = "https://api.nasa.gov/EPIC/api/natural/images/"
    params = {
        "api_key": token_api_nasa
    }
    response = requests.get(nasa_api_epic_url, params=params)
    response.raise_for_status()

    url_get_epic_photo = "https://api.nasa.gov/EPIC/archive/natural"

    urls = []
    for image in response.json():
        image_name = image["image"]
        image_date = datetime.strptime(image["date"], "%Y-%m-%d %H:%M:%S")
        im_date_form = image_date.strftime("%Y/%m/%d")
        elem = f"{url_get_epic_photo}/{im_date_form}/png/{image_name}.png"
        urls.append(elem)

    return urls


def fetch_nasa_epic_photos(token_api_nasa):
    params = {
        "api_key": token_api_nasa
    }
    nasa_epic_urls = get_nasa_epic_urls(token_api_nasa)
    for picture_number, url in enumerate(nasa_epic_urls, start=1):
        response = requests.get(url, params=params)
        response.raise_for_status()
        file_path = f"images/epic{picture_number}.png"
        with open(file_path, 'wb') as file:
            file.write(response.content)


def fetch_nasa_pictures(token_api_nasa):
    nasa_picture_urls = get_nasa_picture_urls(token_api_nasa)
    for picture_number, url in enumerate(nasa_picture_urls, start=1):
        response = requests.get(url)
        response.raise_for_status()

        file_path = f"images/nasa{picture_number}{get_filename_extension(url)}"
        with open(file_path, 'wb') as file:
            file.write(response.content)


if __name__ == "__main__":
    load_dotenv()
    Path("images").mkdir(parents=True, exist_ok=True)
    token_api_nasa = os.getenv("NASA_API_TOKEN")
    fetch_nasa_pictures(token_api_nasa)
