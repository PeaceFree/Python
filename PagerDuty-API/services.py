import json
import csv
import requests

# Setup API Authentication
API_KEY = 'Your API_KEY'
BASE_URL = 'https://api.pagerduty.com/services'
headers = {
    'Authorization': f'Token token={API_KEY}',
    'Accept': 'application/vnd.pagerduty+json;version=2'
}

# convert csv to json
# Escalation_Policies_ID can be obtained from Escalation_Policies
with open ('services.csv', 'r' ) as inMemory:
    reader = csv.reader(inMemory)
    next(reader)
    new = []
    for row in reader:
        new.append({"type":row[0],
                     "name":row[1],
                     "description":row[2],
                     "auto_resolve_timeout":row[3],
                     "escalation_policy": {
                                       "id":"Escalation_Policies_ID",
                                       "type":"escalation_policy_reference"
                                       }
                            }
                      )
   
# API Post Request for each service
for x in new:
    got = requests.post(f'{BASE_URL}', headers=headers, json={"service":x})   
    response = got.json()
    print(response)

