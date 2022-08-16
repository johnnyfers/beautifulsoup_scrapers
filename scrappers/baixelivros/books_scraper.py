import time
from helpers.get_random_string import get_random_string
from helpers.save_csv import save_csv
from bs4 import BeautifulSoup as bs4
from helpers.get_driver import get_driver

driver = get_driver()
url = 'https://www.baixelivros.com.br/acervo/dominio-publico'

books = []

while True:
    try:
        driver = get_driver()
        driver.get(url)
        time.sleep(2)
        html = driver.page_source
        page = bs4(html, 'lxml')
        boxes = page.find_all('div', {'class': 'item-inner clearfix'})

        for box in boxes:
            book = {
                'title': box.find('a', {'class': 'post-url post-title'}).text,
                'link': box.find('a', {'class': 'post-url post-title'})['href'],
                'type': box.find('div', {'class': 'term-badges floated'}).text,
            }
            books.append(book)
        next_page = page.find('a', {'class': 'next page-numbers'})['href']

        print('next page', next_page)
        url = next_page
        driver.close()
        driver.quit()
    except Exception as error:
        print(error)
        break

number_of_characters = 15
filename = get_random_string(number_of_characters) + '.csv'
path = f'files/baixelivros_{filename}'
save_csv(path, books)

'//*[@id="content"]/div/div/div[1]/div[2]/a[4]'