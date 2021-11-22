import os
from urllib.parse import urlsplit


def get_filename_extension(url):
    url_split = urlsplit(url)
    url_path = url_split.path
    filename_extension = os.path.splitext(url_path)[1]

    return filename_extension
