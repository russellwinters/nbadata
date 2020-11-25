# NBA Data

This app is a small comman line tool that fetches NBA data. Currently there is a single command, which fetches the team rosters, by activating running `python3 app.py team <team_abbreviation>`

## Setup

1. First clone this repo, bringing it to your own machine.
2. Navigate to the `nbadata` directory and run `python3 -m venv env` in the command line. This will create a virtual environemnt that will be ignored by github, but will hold all dependencies without installing them globally.
3. Activate the Virtual Environment by running `source env/bin/activate`. This command will activate the vitrual environment and inform pip to install any packages to this local environment as opposed to the global scope on your computer.
4. To install all the dependencies for this app, run `pip install -r requirements.txt`
5. The app should be fully installed and ready to go! With the `venv` activated, run `python3 app.py team phi` to see the full roster for the Philadelphia 76ers!
