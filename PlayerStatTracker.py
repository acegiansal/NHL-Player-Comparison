import requests as req
import json

# Attempts to find players with a matching name
def find_player(name):
    players_info = {
        'quantity': 0, 
        'names': [], 
        'id': [],
        'team': [],
        'number': []
    }
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
                    players_info['quantity'] += 1
                    players_info['names'].append(player['person']["fullName"])
                    players_info['id'].append(player['person']["id"])
                    players_info['team'].append(team['name'])
                    players_info['number'].append(player["jerseyNumber"])
    return players_info

def get_stats(player_info: dict) -> dict:
    print('hello')
    player_stats = {}
    



                    

if __name__ == "__main__":
    testDict = find_player('sebastian aho')
    print (testDict)