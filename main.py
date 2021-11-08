import requests
from pathlib import Path



def uploade_pictures(url, filename):
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)

    return file


def get_pictures_url(request_url):
    response = requests.get(request_url)
    response.raise_for_status()

    return response.json()["links"]["flickr_images"]


if __name__ == "__main__":
    Path("images").mkdir(parents=True, exist_ok=True)
    filename = "images/hubble.jpeg"
    url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    request_url = "https://api.spacexdata.com/v3/launches/67"

    # uploade_pictures(url, filename)
    print(get_pictures_url(request_url))
