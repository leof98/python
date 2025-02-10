# Day 51
# Using selenium to create a twitter bot
# A bot that checks the internet speed and makes a tweet about it

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""
TWITTER_URL = "https://x.com/"
TWITTER_USERNAME = ""

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        time.sleep(6)
        start_bt = self.driver.find_element(By.CLASS_NAME, value='js-start-test')
        start_bt.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(f"Download Speed: {self.down}")
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"Upload Speed: {self.up}")
        pass


    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)

        # Login
        login_bt = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a/div')
        login_bt.click()
        time.sleep(5)
        login_input = self.driver.find_element(By.XPATH, value='/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        login_input.send_keys(TWITTER_EMAIL)
        next_bt = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span')
        next_bt.click()
        time.sleep(6)
        verify_input = self.driver.find_element(By.CSS_SELECTOR, value=".r-30o5oe")
        verify_input.send_keys(TWITTER_USERNAME)
        ok_bt = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button/div')
        ok_bt.click()
        time.sleep(6)
        password_input = self.driver.find_element(By.CSS_SELECTOR, value=".r-homxoj")
        password_input.send_keys(TWITTER_PASSWORD)
        login = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div/span')
        login.click()
        time.sleep(6)

        # Tweeting
        post = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div')
        post.send_keys(f"Hey Internet Provider, why is my internet speed {self.down} down/{self.up} up when I pay for {PROMISED_DOWN} down/{PROMISED_UP} up")
        send_bt = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        send_bt.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
