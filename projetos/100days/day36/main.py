# Day 36
# HTTP Requests
# I had a problem with the free stock API
# *need to revisit this day

import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "stockkey"
NEWS_API_KEY = "apikey"
TWILIO_SID = "mysid"
TWILIO_AUTH_TOKEN = "mytoken"


stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
data = response.json()
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

# Getting the day before yesterday closing price
before_yesterday_data = data_list[1]
before_yesterday_closing_price = before_yesterday_data["4. close"]

difference = abs(float(yesterday_closing_price) - float(before_yesterday_closing_price))

diff_percent = (difference / float(yesterday_closing_price)) * 100

if diff_percent > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+12315599973",
            to="mynumber"
        )
