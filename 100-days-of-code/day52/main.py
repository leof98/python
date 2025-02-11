# Day 52
# Using selenium to create a instagram bot

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

INSTA_URL = "https://instagram.com"
INSTA_TARGET_URL = ""
INSTA_USERNAME = ""
INSTA_PASSWORD = ""



class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(INSTA_URL)
        time.sleep(2)
        username_area = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        username_area.send_keys(INSTA_USERNAME)
        password_area = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        password_area.send_keys(INSTA_PASSWORD)
        login_bt = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[3]/button/div')
        login_bt.click()
        time.sleep(3)

    def find_followers(self):
        time.sleep(2)
        self.driver.get(INSTA_TARGET_URL)
        time.sleep(2)
        followers_list = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a')
        followers_list.click()
        time.sleep(5)
        modal = self.driver.find_element(By.XPATH, value='/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        for i in range(1):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(3)

    def follow(self):
        buttons_list = self.driver.find_elements(By.CSS_SELECTOR, "div.xyi19xy button")
        for button in buttons_list:
            try:
                time.sleep(1)
                button.click()
                time.sleep(15)
            except:
                pass

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
