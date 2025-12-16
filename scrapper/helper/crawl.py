import requests
from urllib.parse import urlparse

from bs4 import BeautifulSoup as bs

def normalize_url(url):
    url_components = urlparse(url)
    full_path = f'{url_components.netloc}{url_components.path}'
    full_path = full_path.rstrip('/')
    return full_path.lower()
  

def soup_html(url):
    norm_url = normalize_url(url)
    response = requests.get(normalize_url)
    return bs(response, 'html_parser')