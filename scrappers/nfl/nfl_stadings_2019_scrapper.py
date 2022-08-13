from helpers.get_html import get_html
from helpers.get_random_string import get_random_string
from helpers.save_csv import save_csv

url = 'https://www.nfl.com/standings/league/2019/PRE'

page = get_html(url)

table = page.find('table',{'class': '''d3-o-table d3-o-table--row-striping d3-o-table--detailed d3-o-standings--detailed d3-o-table--sortable {sortlist: [[4,1]], sortinitialorder: 'desc'}'''})
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

nfl_standings_2019 = []

for body in table_rows:
    nfl_standings_2019_dict = {}
    body_index = table_rows.index(body)
    
    for header in table_headers:
        header_index = table_headers.index(header)
        if (header_index == 0):    
            nfl_standings_2019_dict[header] = table.find_all('div', {'class': 'd3-o-club-fullname'})[body_index].text
        else:
            nfl_standings_2019_dict[header] = body[header_index]

    nfl_standings_2019.append(nfl_standings_2019_dict)

number_of_characters = 15
filename = get_random_string(number_of_characters) + '.csv'
path = f'files/nfl_standings_2019_{filename}'

save_csv(path, nfl_standings_2019)