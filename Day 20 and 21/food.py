from turtle import Turtle
import random

COORDINATES = [260, 220, 180, 140, 100, 60, 20, -20, -60, -100, -140, -180, -220, -260]


# Inherit from Turtle class
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('red')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.setposition(random.choice(COORDINATES), random.choice(COORDINATES))
