from turtle import Turtle
import random as rnd

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_X = rnd.randint(-280, 280)
        random_Y = rnd.randint(-280, 280)
        self.goto(random_X, random_Y)