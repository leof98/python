# Day 35
# Using twilio to send SMS
# Also learning about environment variables

import requests
import os
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWN_API_KEY")
ACCOUNT_SID = "aaa"
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": 23.979577,
    "lon": -46.313418,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=OWM_ENDPOINT,params=parameters)
response.raise_for_status()

rain = False
weather_data =  response.json()
for hour_data in weather_data["list"]:
    weather_code = hour_data["weather"][0]["id"]
    if int(weather_code) < 700:
        rain = True

if rain:
    client = Client(ACCOUNT_SID, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember the umbrella!", from_="+11319999199", to="+5513991999999"
    )
    print(message.status)
