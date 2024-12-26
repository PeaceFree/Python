
INTRODUCTION : 
Step by Step Guide to PagerDuty API integration in Python.
services.py script will allow to bulk create Services in PagerDuty account using the API, with information about the services defined from a services.csv 

Files included in PagerDuty Folder:
services.py
services.csv

............................................................................................................................................

PREREQUISITES : 
Python environment (3.12+ recommended)
PagerDuty account with an API key (obtain from PagerDuty)

Setting Up The Project:
copy PagerDuty folder to local drive
cd into PagerDuty folder in local drive
pip install requests  (windows-> py -m pip install requests)

............................................................................................................................................

Setup API Authentication in services.py:
Example : 

import requests
API_KEY = 'your_api_key_here'
BASE_URL = 'PagerDuty API access gate URL'

headers = {
    'Authorization': f'Token token={API_KEY}',
    'Accept': 'application/vnd.pagerduty+json;version=2'
}

............................................................................................................................................

API Post Request in services.py:
service is replaced as {"service":x} to extract a single service payload from services.csv  
Example : 

 got = requests.post(f'{BASE_URL}', headers=headers, json=service)   
   response = got.json()
   print(response)

............................................................................................................................................

Escalation_Policies_ID can be obtained from Escalation_Policies.
{"service":x} extracts a single service payload to json Example :

          {
           "service": {
              "type": "service",
              "name": "My Web App",
              "description": "My cool web application that does things",
              "auto_resolve_timeout": "14400",
              "escalation_policy": {
                                   "id": "Escalation_Policies_ID",
                                   "type": "escalation_policy_reference"
                                  } 
                        }
           } 

.............................................................................................................................................

Run command in terminal to bulk create Services through PagerDuty API, with information about the services defined in services.csv :   

python services.py (linux-> python3 services.py)

...............................................................Thank You......................................................................

 


