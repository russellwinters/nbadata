from requests import get
from bs4 import BeautifulSoup
import sys
import csv

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
        with open("nba_player_list.csv") as prev_file:
            csv_reader = csv.reader(prev_file, delimiter=',')
            for row in csv_reader:
                if row[0] != "player_id":
                    players.append({"player_id": row[0], "player_name": row[1]})

        for link in target_links:
            split_string = link.split("/")
            single_player = {"player_id": split_string[-2], "player_name": split_string[-1]}
            if not(single_player in players):
                players.append(single_player)

        with open("nba_player_list.csv", "w", encoding="utf-8", newline="") as output_file:
            fc = csv.DictWriter(output_file, fieldnames=["player_id", "player_name"])
            fc.writeheader()
            fc.writerows(players)
        