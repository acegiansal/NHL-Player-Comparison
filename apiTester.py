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

response = req.get("https://statsapi.web.nhl.com/api/v1/people/8476459/stats?stats=gameLog&season=20162017")
print(response.status_code)

jprint(response.json())

