import requests as req
import json

# Team Dictionary
TEAM_ABB = {"ANA":24, 
            "ARI":53,
            "BOS":6,
            "BUF":7,
            "CGY":20,
            "CHI":16,
            "COL":21,
            "CBJ":29,
            "DAL":25,
            "DET":17,
            "EDM":22,
            "FLA":13,
            "LAK":26,
            "MIN":30,
            "MTL":8,
            "NSH":18,
            "NJD":1,
            "NYI":2,
            "NYR":3,
            "OTT":9,
            "PHI":4,
            "PIT":5,
            "SJS":28,
            "SEA":55,
            "STL":19,
            "TBL":14,
            "TOR":10,
            "VAN":23,
            "VGK":54,
            "WSH":15,
            "WPG":52,
            }


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
                    print(f"Found player {target} on the {team['name']} with ID: {player['person']['id']}")
                    players_info['quantity'] += 1
                    players_info['names'].append(player['person']["fullName"])
                    players_info['id'].append(player['person']["id"])
                    players_info['team'].append(team['name'])
                    players_info['number'].append(player["jerseyNumber"])
    return players_info

def find_player_stats(player_id_list: list, YEAR: str) -> dict:
    player_clean_stats = {}
    player_clean_stats['quantity'] = len(player_id_list)
    player_clean_stats['names'] = []
    player_clean_stats['team'] = []
    player_clean_stats['age'] = []
    player_clean_stats['num'] = []
    player_clean_stats['team'] = []
    player_clean_stats['pos'] = []
    player_clean_stats['gp'] = []
    player_clean_stats['g'] = []
    player_clean_stats['a'] = []
    player_clean_stats['p'] = []
    player_clean_stats['pm'] = []
    player_clean_stats['pim'] = []

    for id in player_id_list:
        print(f"Finding stats for player: {id}")
        player_api = req.get(f"https://statsapi.web.nhl.com/api/v1/people/{id}/")
        player_info = json.loads(player_api.text)["people"][0]
        player_clean_stats['names'].append(player_info["fullName"])
        player_clean_stats['age'].append(player_info["currentAge"])
        player_clean_stats['num'].append(player_info['primaryNumber'])
        player_clean_stats['pos'].append(player_info['primaryPosition']['code'])

        for team in TEAM_ABB:
            if TEAM_ABB[team] == player_info['currentTeam']['id']:
                player_clean_stats['team'].append(team)
                break

        player_api = req.get(f"https://statsapi.web.nhl.com/api/v1/people/{id}/stats?stats=statsSingleSeason&season={YEAR}")
        player_mess_stats = json.loads(player_api.text)["stats"][0]["splits"][0]["stat"]
        player_clean_stats['gp'].append(player_mess_stats['games'])
        player_clean_stats['g'].append(player_mess_stats['goals'])
        player_clean_stats['a'].append(player_mess_stats['assists'])
        player_clean_stats['p'].append(player_mess_stats['assists'] + player_mess_stats['goals'])
        player_clean_stats['pm'].append(player_mess_stats['plusMinus'])
        player_clean_stats['pim'].append(player_mess_stats['penaltyMinutes'])

    return player_clean_stats

def get_stats(player_info: dict) -> dict:
    print('hello')
    player_stats = {}
                    

if __name__ == "__main__":
    # Tkachuk ID: 8480801
    test_list = ['8480801', '8480208', '8480064']
    year = '20202021'
    testDict = find_player_stats(test_list, year)
    print (testDict)