import requests 
from bs4 import BeautifulSoup
from pprint import pprint

url = 'https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/all/?sortcol=rutd&sortdir=descending'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

player_rows = soup.find_all('tr')

player_rows = player_rows[1:]

players_array = []

counter = 0

for row in player_rows:

    player_data = {}
    player_name = row.select('a')[1].get_text()
    player_position = row.select('.CellPlayerName-position')[0].get_text()
    player_team = row.select('.CellPlayerName-team')[0].get_text()
    player_running_touchdowns = row.select('td')[2].get_text()
    player_data['name'] = player_name
    player_data['position'] = player_position.strip()
    player_data['team'] = player_team.strip()
    player_data['RUTD'] = player_running_touchdowns.strip()

    players_array.append(player_data)

    counter += 1

    if counter == 20:
        break

pprint(players_array)