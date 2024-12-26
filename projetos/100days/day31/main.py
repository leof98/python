# Day 31
# Capstone Project
# A flash card game to study another language

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    fr_word = current_card["French"]
    canvas.itemconfig(front_card, image=front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=fr_word, fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(front_card, image=back_img)
    en_word = current_card["English"]
    canvas.itemconfig(card_word, text=en_word, fill="white")

def remove_card():
    if current_card in to_learn:
        to_learn.remove(current_card)
        next_card()
        new_data = pandas.DataFrame(to_learn)
        new_data.to_csv("data/words_to_learn", index=False)
    else:
        pass

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=850, height=550)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
front_card = canvas.create_image(425, 275, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(425, 160, text="", font=("Arial", 35, "italic"))
card_word = canvas.create_text(425, 280, text="", font=("Arial", 50, "bold"))

# Buttons
right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0,command=remove_card)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()
window.mainloop()
