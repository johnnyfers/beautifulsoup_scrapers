def ask():
    return input('''welcome to web scrapping plataform, please choose an option: \n
    1. phones scrapper \n
    2. apple scrapper\n
    3. world population scrapper\n
    4. cancel
    ''')


if __name__ == '__main__':
    option = ask()
    while (option != '4'):
        if option == '1':
            import scrappers.webscraper.phones_scrapper

        if option == '2':
            import scrappers.marketwatch.apple_scrapper

        if option == '3':
            import scrappers.worldometer.world_population_scrapper

        option = ask()

        print('invalid option')
