# Day 18
# Hirst painting - Project Day 18
import turtle
from turtle import *
import random

color_list = [(1, 9, 30), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165)]
tim = Turtle()
colormode(255)
tim.speed(10)
tim.penup()
tim.hideturtle()
tim.goto(-250, -200)
y_location = -200
for i in range(10):
    y_location += 50
    for y in range(10):
        random_color = random.choice(color_list)
        tim.dot(20, random_color)
        tim.forward(50)
    tim.goto(-250, y_location)

screen = Screen()
screen.exitonclick()
