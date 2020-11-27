from requests import get
from bs4 import BeautifulSoup
import csv


def fetch_player(player):
    # Format Player site for scraping ESPN
    url = ""
    with open("nba_player_list.csv") as player_list:
        file = csv.reader(player_list, delimiter=',')
        for row in file:
            if(row[1] == player.replace(" ", "-").lower()):
                url = f"https://www.espn.com/nba/player/_/id/{row[0]}/{row[1]}"
    
    if(url == ""):
        print("Could not find that player.")
    else:
        # Fetch Site and create soup
        printList = [f"Player: {player}"]
        site = get(url)
        soup = BeautifulSoup(site.text, 'html.parser')
        name = soup.find_all("ul", class_=True)
        for list in name:
            if "StatBlock" in str(list):
                divs = list.find_all("div")
                for div in divs:
                    if "Points Per Game" in str(div) and div.nextSibling:
                        printList.append(f"PPG: {div.nextSibling.text}")
                    if "Rebounds Per Game" in str(div) and div.nextSibling:
                        printList.append(f"RPG: {div.nextSibling.text}")
                    if "Assists Per Game" in str(div) and div.nextSibling:
                        printList.append(f"APG: {div.nextSibling.text}")
                    if "Player Efficiency Rating" in str(div) and div.nextSibling:
                        printList.append(f"PER: {div.nextSibling.text}")
        
        for item in printList:
            print(item)
    

