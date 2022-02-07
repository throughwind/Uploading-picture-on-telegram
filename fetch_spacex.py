import requests
from pathlib import Path
from filemane_extension import get_filename_extension


def get_spacex_pictures_url():
    spacex_api_url = "https://api.spacexdata.com/v3/launches/67"
    response = requests.get(spacex_api_url)
    response.raise_for_status()

    return response.json()["links"]["flickr_images"]


def fetch_spacex_last_launch():
    spasex_pictures_urls = get_spacex_pictures_url()
    for i, url in enumerate(spasex_pictures_urls, start=1):
        response = requests.get(url)
        response.raise_for_status()

        filename = f"images/spacex{i}{get_filename_extension(url)}"
        with open(filename, 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    Path("images").mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch()
