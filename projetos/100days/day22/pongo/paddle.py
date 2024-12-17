# Day 22
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1, outline=1)
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 35
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 35
        self.goto(self.xcor(), new_y)
