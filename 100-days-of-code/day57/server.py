# Day 57
# more on web dev with flask
# Using interactive html with Jinja,

from flask import Flask, render_template
import requests
import random
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    random_num = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_num, year=current_year)

@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url).json()
    gender = gender_response["gender"]
    age_url = f"https://api.agify.io?name={name}"
    response = requests.get(age_url).json()
    age = response["age"]

    return render_template("guess.html", name=name, age=age, gender=gender)

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
