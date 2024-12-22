# Day 27
from tkinter import *

window = Tk()
window.title("Miles to Km")
window.minsize(width=150, height=100)
window.config(padx=30, pady=30)

def button_clicked():
    miles_input = float(user_input.get())
    converted = round(miles_input * 1.609)
    result.config(text=converted)

# Label

miles_label = Label(text="Miles", font=("Arial", 12))
km_label = Label(text="Km", font=("Arial", 12))
miles_label.grid(column=2, row=0)
km_label.grid(column=2, row=1)
equals_label = Label(text="=", font=("Arial", 12))
equals_label.grid(column=0, row=1)
result = Label(text="0", font=("Arial", 12))
result.grid(column=1, row=1)

# Entry
user_input = Entry(width=5)
user_input.grid(column=1, row=0)

# Button

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()
