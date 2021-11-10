import requests
from pathlib import Path



def get_pictures_url(request_url):
    response = requests.get(request_url)
    response.raise_for_status()

    return response.json()["links"]["flickr_images"]


def uploade_pictures(urls):
    for i, pictures_url in enumerate(urls):
        response = requests.get(pictures_url)
        response.raise_for_status()

        filename = f"images/spacex{i + 1}.jpg"
        with open(filename, 'wb') as file:
            file.write(response.content)

    return file



if __name__ == "__main__":
    Path("images").mkdir(parents=True, exist_ok=True)
    
    # url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    request_url = "https://api.spacexdata.com/v3/launches/67"
    urls = get_pictures_url(request_url)
    uploade_pictures(urls)
