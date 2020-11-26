from rosters import fetch_roster, ShowTeamAbbrevs
import sys


def main():

    args = sys.argv

    if len(sys.argv) > 1:  # Check to see if arguement was given

        if(args[1] == "team" and len(args) == 3):
            fetch_roster(args[2])

        elif(args[1]) == 'show':
            ShowTeamAbbrevs()


  
    else:
        print("Only team Rosters are supported at the moment. To search for a roster enter 'python3 app.py team <team abbreviation>'")

if __name__ == '__main__':
    main()