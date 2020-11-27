from rosters import fetch_roster, ShowTeamAbbrevs
from add_players import add_players_from_roster
from players import fetch_player
import sys

args = sys.argv

if(args[1] == "team" and len(args) == 3):
    fetch_roster(args[2])
elif (args[1] == "add_players" and len(args) == 3):
    add_players_from_roster(args[2])
	
elif (args[1] == 'show'):
    ShowTeamAbbrevs()

elif(args[1] == "player"):
    if(len(args) == 4):
        player = f"{args[2]} {args[3]}"
        fetch_player(player)
    else:
        print("Please enter a full name")
	
else: 
    print("Only team Rosters are supported at the moment. To search for a roster enter 'python3 app.py team <team abbreviation>'")
	