import requests
from urllib.parse import urlparse


def normalize_url(url):
    url_components = urlparse(url)
    full_path = f'{url_components.netloc}{url_components.path}'
    full_path = full_path.rstrip('/')
    return full_path.lower()
  

def get_html(url):
    '''norm_url = normalize_url(url)
    response = requests.get(normalize_url)
    '''
    try: 
        response = requests.get(url, headers={'User-Agent': 'PracticeScrapping/1.0'})
        if response.status_code >= 400:
            raise Exception(f"Error: Status code {response.status_code}")
    
        content_type = response.headers.get('content-type', '')
        if 'text/html' not in content_type:
            raise Exception(f"Error: Expected text/html but got {content_type}")
        
        return response.text
    
    except requests.exceptions.RequestException as e:
        raise Exception('fThere was an error: {e}')