import requests
from pathlib import Path



def get_spacex_pictures_url(request_spacex_url):
    response = requests.get(request_spacex_url)
    response.raise_for_status()

    return response.json()["links"]["flickr_images"]


def fetch_spacex_last_launch(spasex_pictures_urls):
    for i, pictures_url in enumerate(spasex_pictures_urls):
        response = requests.get(pictures_url)
        response.raise_for_status()

        filename = f"images/spacex{i + 1}.jpg"
        with open(filename, 'wb') as file:
            file.write(response.content)

    return file



if __name__ == "__main__":
    Path("images").mkdir(parents=True, exist_ok=True)
    request_spacex_url = "https://api.spacexdata.com/v3/launches/67"
    spasex_pictures_urls = get_spacex_pictures_url(request_spacex_url)
    fetch_spacex_last_launch(spasex_pictures_urls)
