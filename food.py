from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.speed('fastest')
        self.color('blue')
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.refresh()

    def refresh(self):
        x_position = random.randint(-280, 280)
        y_position = random.randint(-280, 280)
        self.goto(x_position, y_position)


    def move_up(self):
        self.setheading(27)
