def ask():
    return input('''welcome to web scrapping plataform, please choose an option: \n
    1. phones scrapper \n
    2. apple scrapper\n
    3. world population scrapper\n
    4. nfl 2019 standings\n
    5. airbnb MIAMI \n
    6. cancel \n
    ''')


if __name__ == '__main__':
    option = ask()
    while True:
        if option == '1':
            import scrappers.webscraper.phones_scrapper
        elif option == '2':
            import scrappers.marketwatch.apple_scrapper
        elif option == '3':
            import scrappers.worldometer.world_population_scrapper
        elif option == '4':
            import scrappers.nfl.nfl_stadings_2019_scrapper
        elif option == '5':
            import scrappers.airbnb.airnbnb_miami_scrapper
        elif option == '6':
            print('bye')
            break
        else:
            print('invalid option')
        
        option = ask()

