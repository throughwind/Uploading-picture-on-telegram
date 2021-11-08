import requests
from pathlib import Path



def uploade_pictures(url, filename):
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)

    return file

if __name__ == "__main__":
    Path("files").mkdir(parents=True, exist_ok=True)
    filename = "files/hubble.jpeg"
    url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"

    uploade_pictures(url, filename)
