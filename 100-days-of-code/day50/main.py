from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Day 50
# more on selenium
# Tinder swipe bot
# impossible to complete with the new tinder login system


tinder_url = ""
USERNAME = ""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get(tinder_url)
time.sleep(1)

# cookies = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div')
# cookies.click()

login = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
login.click()
time.sleep(3)
login_google = driver.find_element(By.XPATH, value='/html/body/div/div/div[2]/span[1]')
login_google.click()

# id_space = driver.find_element(By.ID, value="identifierId")
# id_space.send_keys(USERNAME)

# next_bt = driver.find_element(By.XPATH, value='//*[@id="identifierNext"]/div/button/span')
# next_bt.click()
