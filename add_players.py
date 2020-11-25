from requests import get
from bs4 import BeautifulSoup
import sys

def add_players_from_roster(team_abbreviation):
    site = get("https://www.espn.com/nba/team/roster/_/name/{}".format(team_abbreviation))
    soup = BeautifulSoup(site.text, 'html.parser')

    links = soup.find_all("a")

    target_text = "player/_/id"
    target_links = []

    for link in links:
        href = link.get('href')
        if isinstance(href, str) and target_text in href: 
            target_links.append(href)

    if len(target_links) == 0:
        print("The team abbreviation you entered is not valid.")
    else:
        players = []

        for link in target_links:
            split_string = link.split("/")
            single_player = {split_string[-2]: split_string[-1]}
            if not(single_player in players):
                players.append(single_player)
        
        prior_dictionary = {"2384": "dwight-howard", "6440": "tobias-harris"}

        for player in players: 
            if not(set(player).issubset(set(prior_dictionary))):
                prior_dictionary.update(player)
        
        for key in prior_dictionary:
            print({"key": key, "value": prior_dictionary[key]})