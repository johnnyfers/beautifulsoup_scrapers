from helpers.get_html import get_html
from helpers.get_random_string import get_random_string
from helpers.save_csv import save_csv

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

page = get_html(url)
divs = page.find_all('div',{'class':'col-sm-4 col-lg-4 col-md-4'})
phones = []

for div in divs:
    phone_dict = {
        'name': div.find('a', {'class':'title'}).text,
        'price': div.find('h4', {'class':'pull-right price'}).text,
        'description':  div.find('p', {'class':'description'}).text,
        'ratings': div.find('p', {'class':'pull-right'}).text,
    }
    phones.append(phone_dict)

number_of_characters = 15
filename = get_random_string(number_of_characters) + '.csv'
path = f'files/phones_{filename}'

save_csv(path, phones)