import requests
from bs4 import BeautifulSoup as bs

def get_html(url):
    page = requests.get(url)
    soup = bs(page.text, 'lxml')

    return soup