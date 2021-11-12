import os
from urllib.parse import urlsplit



def get_filename_extension(url):
    url_split = urlsplit(url)
    url_path = url_split.path
    name_file = os.path.split(url_path)[1]
    filename_extension = os.path.splitext(name_file)[1]

    return filename_extension
