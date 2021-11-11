import requests
import os
from pathlib import Path
from urllib.parse import urlsplit
from dotenv import load_dotenv
from datetime import datetime



def get_spacex_pictures_url(spacex_api_url):
    response = requests.get(spacex_api_url)
    response.raise_for_status()

    return response.json()["links"]["flickr_images"]

def get_nasa_picture_urls(nasa_api_url):
    params = {
        "start_date": "2021-10-01",
        "end_date": "2021-11-01",
        "api_key": token_api_nasa
}
    response = requests.get(nasa_api_url, params=params)
    response.raise_for_status()
    urls_list = [url.get("url") for url in response.json()]

    return urls_list

def get_filename_extension(url):
    url_split = urlsplit(url)
    url_path = url_split.path
    name_file = os.path.split(url_path)[1]
    filename_extension = os.path.splitext(name_file)[1]

    return filename_extension

def get_urls_nasa_epic(nasa_api_epic_url):
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


def fetch_nasa_epic_photo(nasa_epic_urls):
    params = {
        "api_key": token_api_nasa
    }
    for i, url in enumerate(nasa_epic_urls):
        response = requests.get(url, params=params)
        response.raise_for_status()
        filename = f"images/epic{i + 1}.png"
        with open(filename, 'wb') as file:
            file.write(response.content)

    return file


def fetch_nasa_pictures(nasa_picture_urls):
    for i, url in enumerate(nasa_picture_urls):
        response = requests.get(url)
        response.raise_for_status()

        filename = f"images/nasa{i + 1}{get_filename_extension(url)}"
        with open(filename, 'wb') as file:
            file.write(response.content)

    return file

def fetch_spacex_last_launch(spasex_pictures_urls):
    for i, url in enumerate(spasex_pictures_urls):
        response = requests.get(url)
        response.raise_for_status()

        filename = f"images/spacex{i + 1}{get_filename_extension(url)}"
        with open(filename, 'wb') as file:
            file.write(response.content)

    return file


if __name__ == "__main__":
    load_dotenv()
    token_api_nasa = os.getenv("NASA_API_TOKEN")
    Path("images").mkdir(parents=True, exist_ok=True)
    spacex_api_url = "https://api.spacexdata.com/v3/launches/67"
    nasa_api_url = "https://api.nasa.gov/planetary/apod"
    nasa_api_epic_url = "https://api.nasa.gov/EPIC/api/natural/images/"
    spasex_pictures_urls = get_spacex_pictures_url(spacex_api_url)
    nasa_picture_urls = get_nasa_picture_urls(nasa_api_url)
    nasa_epic_urls = get_urls_nasa_epic(nasa_api_epic_url)
    fetch_spacex_last_launch(spasex_pictures_urls)
    fetch_nasa_pictures(nasa_picture_urls)
    fetch_nasa_epic_photo(nasa_epic_urls)
