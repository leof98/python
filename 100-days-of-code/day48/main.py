# Day 48
# Project of day 48 - Using Selenium to create a click bot for a web game

from selenium.webdriver.common.by import By
from selenium import webdriver
import time

game_url = "http://orteil.dashnet.org/experiments/cookie/ "

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(game_url)

cookie = driver.find_element(By.ID, value="cookie")
items = driver.find_elements(By.CSS_SELECTOR, value ="#store div")
items_id = [item.get_attribute("id") for item in items]
timeout = time.time() + 10
max_time = time.time() + 60*5

print(items_id)
while True:
    cookie.click()

    # Every 5 seconds
    # Check the current balance
    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        prices = []

        # Getting the price for each item
        for price in all_prices:
            item_text = price.text
            if item_text != "":
                cost = int(item_text.split("-")[1].strip().replace(",", ""))
                prices.append(cost)

        # Making a dict with each id and price
        items_dict = {}
        for n in range(len(prices)):
            items_dict[prices[n]] = items_id[n]

        # Getting the current balance value
        balance = driver.find_element(By.ID, value="money").text
        if "," in balance:
            balance.replace(",", "")
        current_balance = int(balance)
        print(current_balance)

        # Getting the most expensive affordable item, and buying it
        affordable = {}
        for cost, id in items_dict.items():
            if current_balance >= cost:
                affordable[cost] = id
        print(affordable)
        if len(affordable) > 0:
            highest_affordable = max(affordable)
            buy_this = driver.find_element(By.ID, value=affordable[highest_affordable])
            buy_this.click()

        # Resetting the timeout
        timeout = time.time() + 5

    # End the script
    if time.time() > max_time:
        cps = driver.find_element(By.ID, value="cps").text.split(":")[1].strip()
        print("=====/ Final Score /======")
        print(f"Cookies per second = {cps}")
        break

driver.quit()
