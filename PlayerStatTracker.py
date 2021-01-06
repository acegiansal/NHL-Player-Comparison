import requests as req
import json

# Attempts to find players with a matching name
def find_player(name):
    test = 0
    target = name.lower()
    team_api = req.get("https://statsapi.web.nhl.com/api/v1/teams/")
    franchises = json.loads(team_api.text)["teams"]
    for team in franchises:
        if team['active']:
            roster_api = req.get(f"https://statsapi.web.nhl.com/api/v1/teams/{team['id']}/roster")
            roster = json.loads(roster_api.text)["roster"]
            for player in roster:
                if player['person']["fullName"].lower() == target:
                    print(f"Found player {target} on the {team['name']}")

if __name__ == "__main__":
    find_player('Tim stuetzle')