from scrappers.webscraper import phones_scrapper
from scrappers.marketwatch import apple_scrapper


if __name__ == '__main__':
    # get data from https://webscraper.io/test-sites/e-commerce/allinone/phones/touch
    phones_scrapper

    # get data from https://www.marketwatch.com/investing/stock/aapl?mod=search_symbolh
    apple_scrapper