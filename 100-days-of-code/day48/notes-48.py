# Day 48
# Selenium WebDriver
from selenium.webdriver.common.by import By
from selenium import webdriver


# Keep browsers running
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# # Finding an element by name
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# # Finding an element by id
# button = driver.find_element(By.ID, value="submit")
# print(button.size)

# # Getting an element by xpath
# bug_link = driver.find_element(By.XPATH, value='')

menu_info = driver.find_element(By.CSS_SELECTOR,value=".event-widget .shrubbery .menu")
list_items = menu_info.find_elements(By.TAG_NAME, value="li")

list_dict = []
for item in list_items:
    new_dict = {"time": item.text.splitlines()[0], "name": item.text.splitlines()[1]}
    list_dict.append(new_dict)

final_dict = {n: list_dict[n] for n in range(4)}
print(final_dict)

## Close closes one tab
# driver.close()
## Quit closes all tabs

# n_articles = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/ul/li[2]/a[1]')

# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
#
# # Find element by Link text
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# driver.maximize_window()
# # Find the 'Search' <input> by name
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)

# first_name = driver.find_element(By.NAME, value="fName")
# first_name.send_keys("John")
# last_name = driver.find_element(By.NAME, value="lName")
# last_name.send_keys("Doe")
# email = driver.find_element(By.NAME, value="email")
# email.send_keys("john@doe.com")
# submit_button = driver.find_element(By.CLASS_NAME, value="btn-primary")
# submit_button.click()

driver.quit()
