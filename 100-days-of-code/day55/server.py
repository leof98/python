# Day 55
# more on flask

from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def title():
    return ('<h1 style="text-align: center">Guess a number between 0 and 9</h1>'
            '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExczBha210Y25ra3hzbXd3bjNsM2s0amZuMjFjdXYyb2R4Y3RuZTJtaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l378khQxt68syiWJy/giphy.gif"</img>')


random_num =  random.randint(0, 9)

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_num:
        return ('<h1>Too high, try again!</h1>'
                '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXd0bm13Y3JteWl4eWk1bmhmdWNjaHphN29leG03YzJlZm12ZzRnOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VbnUQpnihPSIgIXuZv/giphy.gif"</img>')

    elif guess < random_num:
        return ('<h1>Too Low, try again!</h1>'
                '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDRzZmllMnJkYWV6bmJuejNyeDVjNTZ6MjB3ejY4OWR2NjltOXZqeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/rho9L4MsYXaec/giphy.gif"</img>')

    else:
        return ('<h1>You found me!</h1>'
                '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWp4MnVvOTE3a2VkemIyOHB2ZzJlaW16eXM5aHUwN2F2M2toZnhoMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vFKqnCdLPNOKc/giphy.gif"</img>')


if __name__ == "__main__":
    app.run(debug=True)
