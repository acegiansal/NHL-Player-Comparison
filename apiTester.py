import requests as req
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# for player stats:
# https://statsapi.web.nhl.com/api/v1/people/8476459/stats?stats=statsSingleSeason&season=20182019

## For Roster:
# https://statsapi.web.nhl.com/api/v1/teams/9/roster

response = req.get("https://statsapi.web.nhl.com/api/v1/people/8476459/stats?stats=statsSingleSeason&season=20182019")

# response = req.get("https://statsapi.web.nhl.com/api/v1/people/8476459/")


# response = req.get("https://statsapi.web.nhl.com/api/v1/teams/")

# print(response.status_code)
#jprint(response.json())

# json_data = json.loads(response.text)["stats"][0]["splits"][0]["stat"]
json_data = json.loads(response.text)
# json_data = json.loads(response.text)["people"][0]["currentAge"]

'''
teams = json_data['teams']

for team in teams:
    print(f"Team: {team['abbreviation']}\tID:{team['id']}")
'''
'''
counter = 0
for player in json_data:
    counter += 1
print(counter)
'''

#team_info = json_data['people'][0]['currentTeam']
#print(team_info)
print((json_data))
#print(json_data["birthCity"])
