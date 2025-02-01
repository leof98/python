# Day 45
from bs4 import BeautifulSoup
import requests

# Getting the news article most voted on the web page

response = requests.get("http://news.ycombinator.com/news")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article in articles:
    article_tag = article.find(name="a")
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)


article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

most_votes = article_upvote.index(max(article_upvote))
print(article_texts[most_votes])
print(article_links[most_votes])







# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # Getting the title from the html file.
# print(soup.title.string)

#print(soup.prettify())
#print(soup.a)
# all_anchor_tags  = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# # Getting info by id/class
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
