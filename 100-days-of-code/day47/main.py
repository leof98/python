# Day 47
# Using Beautiful Soup (Web Scraping) and smtplib to send an email alert if the price of a product is below the target

from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

practice_url = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
TARGET_PRICE = 100.00

# Load environment variables
load_dotenv()

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/116.0.0.0",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

response = requests.get(URL, headers=header)

soup = BeautifulSoup(response.text, "html.parser")

price_list = soup.find_all("span", class_="a-offscreen")
title = soup.find("span", id="productTitle")
product_name = title.text

price = price_list[0].text.split("$")[1]
product_price = float(price)
print(product_price)

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(os.environ["MY_EMAIL"], os.environ["MY_PASSWORD"])

if product_price < TARGET_PRICE:
    connection.sendmail(from_addr=os.environ["MY_EMAIL"],
                        to_addrs="l010191@yahoo.com",
                        msg=f"Subject:Amazon Price Alert!\n\n {product_name} is now ${product_price} \n{URL}".encode("utf-8"))
else:
    pass

connection.close()
