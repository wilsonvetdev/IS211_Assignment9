import requests 
from bs4 import BeautifulSoup
from pprint import pprint

url = 'http://www.footballlocks.com/nfl_point_spreads.shtml'

page_response = requests.get(url)

page = page_response.content

soup = BeautifulSoup(page, 'html.parser')

table_rows = soup.select('table')

print(table_rows[37])

# website is a mess, not sure of requirement.