from rosters import fetch_roster
import sys

args = sys.argv

if(args[1] == "team" and len(args) == 3):
    fetch_roster(args[2])
else:
    print("Only team Rosters are supported at the moment. To search for a roster enter 'python3 app.py team <team abbreviation>'")
 