import requests
import os
from pathlib import Path
from urllib.parse import urlsplit
from dotenv import load_dotenv



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

def fetch_nasa_pictures(nasa_picture_urls):
    for i, url in enumerate(nasa_picture_urls):
        response = requests.get(url)
        response.raise_for_status()

        filename = f"images/nasa{i + 1}{get_filename_extension(url)}"
        with open(filename, 'wb') as file:
            file.write(response.content)

    return file

def fetch_spacex_last_launch(spasex_pictures_urls):
    for i, pictures_url in enumerate(spasex_pictures_urls):
        response = requests.get(pictures_url)
        response.raise_for_status()

        filename = f"images/spacex{i + 1}.jpg"
        with open(filename, 'wb') as file:
            file.write(response.content)

    return file


if __name__ == "__main__":
    load_dotenv()
    token_api_nasa = os.getenv("NASA_API_TOKEN")
    Path("images").mkdir(parents=True, exist_ok=True)
    spacex_api_url = "https://api.spacexdata.com/v3/launches/67"
    nasa_api_url = "https://api.nasa.gov/planetary/apod"
    spasex_pictures_urls = get_spacex_pictures_url(spacex_api_url)
    nasa_picture_urls = get_nasa_picture_urls(nasa_api_url)
    fetch_spacex_last_launch(spasex_pictures_urls)
    fetch_nasa_pictures(nasa_picture_urls)
