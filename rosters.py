from requests import get
from bs4 import BeautifulSoup
import sys

def fetch_roster(team_Abbreviation): 
    site = get("https://www.espn.com/nba/team/roster/_/name/{}".format(team_Abbreviation))
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
            player = split_string[-1]
            if not(player in players):
                players.append(player)


        for x in range(len(players)):
            split_player = players[x].split("-")
            split_player[0] = split_player[0].capitalize()
            split_player[1] = split_player[1].capitalize()
            players[x] = " ".join(split_player)


        print(players)

