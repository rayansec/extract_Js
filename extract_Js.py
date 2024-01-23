import requests
from bs4 import BeautifulSoup
import re

def get_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    tag = soup.find_all('script')

    js_urls = [i.get("src") for i in tag if i.get("src") and re.search(r'\.js$', i.get("src"))]

    for js_url in js_urls:
        print(js_url)

get_page(input("Enter the target: "))
