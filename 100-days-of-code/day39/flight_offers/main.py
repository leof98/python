# Day 39
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests

AMADEUS_API_KEY = ""
AMADEUS_API_SECRET = ""

url = "https://test.api.amadeus.com/v1/security/oauth2/token"

data = {
    'grant_type': 'client_credentials',
    'client_id': AMADEUS_API_KEY,
    'client_secret': AMADEUS_API_SECRET
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.post(url, data=data, headers=headers)
print(response.text)
