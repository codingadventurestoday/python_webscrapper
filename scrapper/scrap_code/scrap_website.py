from urllib.parse import urljoin

from bs4 import BeautifulSoup as bs

#from helper.crawl import soup_html

def get_h1_from_html(html):
    soup = bs(html, 'html.parser')

    first_h1 = soup.find('h1')
    return first_h1.get_text()

def get_first_paragraph_from_html(html):
    soup = bs(html, 'html.parser')

    main_tag = soup.find('main')
    if main_tag:
        first_paragraph = main_tag.find('p')
         
    else:
        first_paragraph = soup.find('p')
    return first_paragraph.get_text()

def get_urls_from_html(html, base_url):
    soup = bs(html, 'html.parser')
    all_anchors = soup.find_all('a')
    if all_anchors is None:
        return []

    results = []
    for anchor in all_anchors:
        href = anchor.get('href')
        if href:
            abs_url = urljoin(base_url,href)
            results.append(abs_url)
    return results
    
def get_images_from_html(html, base_url):
    soup = bs(html, 'html.parser')
    all_img = soup.find_all('img')
    if all_img is None: 
        return [] 

    results = []
    for img in all_img:
        source = img.get('src')
        if source:
            abs_url = urljoin(base_url, source)
            results.append(abs_url)
    return results

def extract_page_data(html, page_url):
    results = {}

    results['url'] = page_url
    results['h1'] = get_h1_from_html(html)
    results['first_paragraph'] = get_first_paragraph_from_html(html)
    results['outgoing_links'] = get_urls_from_html(html, page_url)
    results['image_urls'] = get_images_from_html(html, page_url)

    return results