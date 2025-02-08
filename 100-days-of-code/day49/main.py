# Day 49
# Using selenium to create a bot that applies for jobs on linkedin

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

URL = "https://www.linkedin.com/jobs/search/?currentJobId=4068807736&f_AL=true&f_E=1&geoId=106057199&keywords=data%20science&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true&sortBy=R"
EMAIL = ""
PASSWORD = ""

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)
time.sleep(1)
# Log in
login_button = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
login_button.click()
email_field = driver.find_element(By.ID, value="base-sign-in-modal_session_key")
email_field.send_keys(EMAIL)
password_field = driver.find_element(By.ID, value="base-sign-in-modal_session_password")
password_field.send_keys(PASSWORD)
login_button2 = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
login_button2.click()

# Easy apply button
# apply_button = driver.find_element(By.XPATH, value='//*[@id="ember52"]/span')
# apply_button.click()
# Phone field
# save_button.click()
job_list = driver.find_elements(By.CLASS_NAME, value="job-card-list__title--link")
for item in job_list:
    item.click()
    try:
        save_button = driver.find_element(By.CLASS_NAME, value="jobs-save-button__text")

    except NoSuchElementException:
        continue
