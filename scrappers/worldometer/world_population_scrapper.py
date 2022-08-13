from helpers.get_html import get_html
from helpers.get_random_string import get_random_string
from helpers.save_csv import save_csv

url = 'https://www.worldometers.info/world-population/#total'

page = get_html(url)

table = page.find('table',{'class': 'table table-striped table-bordered table-hover table-condensed table-list'})
table_headers = []

for header in table.find_all('th'):
    title = header.text
    table_headers.append(title)

table_rows = []
for row in table.find_all('tr'):
    table_row = []
    for cell in row.find_all('td'):
        table_row.append(cell.text)
    table_rows.append(table_row)
table_rows.pop(0)

world_population = []

for body in table_rows:
    world_population_dict = {}
    for header in table_headers:
        header_index = table_headers.index(header)
        world_population_dict[header] = body[header_index]

    world_population.append(world_population_dict)

number_of_characters = 15
filename = get_random_string(number_of_characters) + '.csv'
path = f'files/world_population_{filename}'

save_csv(path, world_population)