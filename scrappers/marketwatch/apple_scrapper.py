from helpers.get_html import get_html
from helpers.get_random_string import get_random_string
from helpers.save_csv import save_csv

url = 'https://www.marketwatch.com/investing/stock/aapl?mod=search_symbolh'
page = get_html(url)

current_price = page.find('h2', {'class':'intraday__price'}).text
close_price = page.find('td', {'class':'table__cell u-semi'}).text
lower_week_range = page.find_all('span', {'class':'primary'})[4].text
higher_week_range = page.find_all('span', {'class':'primary'})[5].text
current_analyst_rating = page.find('li', {'class':'analyst__option active'}).text

apple_stock = {
    'current_price': current_price.replace('\n', ''),
    'close_price': close_price,
    'lower_week_range_52': lower_week_range,
    'higher_week_range_52': higher_week_range,
    'current_analyst_rating': current_analyst_rating,
}

number_of_characters = 15
filename = get_random_string(number_of_characters) + '.csv'
path = f'files/apple_stock_{filename}'

save_csv(path, [apple_stock])