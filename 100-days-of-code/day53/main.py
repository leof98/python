# Day 53
# Project using BeautifulSoup and Selenium
# Scrap a page for info about apartments/houses and fill a form with it.

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfIb3-w0IXy92qVDBfD1RRjiTddfRSTKMu9LQfotrqTOm917g/viewform?usp=header"
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/116.0.0.0",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

response = requests.get(ZILLOW_URL, headers=header)

soup = BeautifulSoup(response.text, "html.parser")

# Extract links
all_links = soup.find("ul", class_="List-c11n-8-84-3-photo-cards")

double_link_list = [a["href"] for a in all_links.find_all("a", href=True)] if all_links else []
link_list =[]
for item in double_link_list:
    if item not in link_list:
        link_list.append(item)
print(link_list)

# Price
all_prices = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
price_list = []
for price in all_prices:
    price_list.append(price.text)

# Address
all_addresses = soup.find_all("address")
address_list = []
for address in all_addresses:
    address_list.append(address.getText().strip().replace(",", ""))

# Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for i in range(len(link_list)):
    driver.get(FORM_URL)
    time.sleep(3)
    address_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(address_list[i])
    time.sleep(1)
    price_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(price_list[i])
    time.sleep(1)
    link_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(link_list[i])
    time.sleep(1)
    ok_bt = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    ok_bt.click()
