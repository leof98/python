# Day 18
# Learning about turtle library
import turtle
from turtle import *
import random

timmy = Turtle()

colormode(255)
def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

# Shapes
# def draw_shape(sides):
#     timmy.pencolor(change_color())
#     angle = 360 / sides
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# for i in range(3, 11):
#     draw_shape(i)

# Random Walk
# directions = [0, 90, 180, 270]
# timmy.pensize(15)
# timmy.speed(5)
# for i in range(150):
#     timmy.pencolor(change_color())
#     direction = random.choice(directions)
#     timmy.setheading(direction)
#     timmy.forward(35)

# Spirograph
timmy.speed(100)
def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        timmy.circle(100, 360)
        timmy.color(change_color())
        current_heading = timmy.heading()
        timmy.setheading(current_heading + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
