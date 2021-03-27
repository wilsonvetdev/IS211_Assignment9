import requests 
from bs4 import BeautifulSoup
from pprint import pprint

if __name__ == '__main__':
        
    url = 'https://www.nasdaq.com/market-activity/stocks/aapl/historical'

    page_response = requests.get(url)

    # page = page_response.content

    # soup = BeautifulSoup(page, 'html.parser')

    # print(soup)

    print(page_response.status_code) # hung up on terminal, doesn't work and had to interrupt with keyboard.