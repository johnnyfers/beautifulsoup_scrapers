from helpers.get_html import get_html
from helpers.get_random_string import get_random_string
from helpers.save_csv import save_csv

base_url = 'https://www.airbnb.com.br'
url = 'https://www.airbnb.com.br/s/Miami-Beach--FL--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&place_id=ChIJud3-Kxem2YgR62OUJUEXvjc&date_picker_type=calendar&checkin=2022-08-29&checkout=2022-09-27&source=structured_search_input_header&search_type=user_map_move&ne_lat=27.48312235735761&ne_lng=-76.55604491895679&sw_lat=23.8850278868663&sw_lng=-81.17579589551929&zoom=8&search_by_map=true'

posts = []

while True:
    try:
        page = get_html(url)
        boxes = page.find_all('div', {'class': 'c4mnd7m dir dir-ltr'})
        for box in boxes:
            post = {
                'title': box.find('div', {'class': 't1jojoys dir dir-ltr'}).text,
                'link': base_url + box.find('a', {'class': 'ln2bl2p dir dir-ltr'})['href'],
                'price': box.find('span', {'class': 'a8jt5op dir dir-ltr'}).text,
                'rating': box.find('span', {'class': 'ru0q88m dir dir-ltr'}).text,
            }
            posts.append(post)
        
        next_page = base_url + page.find('a', {'aria-label': 'Próximo'})['href']
        url = next_page
    except:
        break

number_of_characters = 15
filename = get_random_string(number_of_characters) + '.csv'
path = f'files/airbnb_miami_{filename}'
save_csv(path, posts)