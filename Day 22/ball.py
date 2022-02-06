from turtle import Turtle
import random

start_directions = [10, -10]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.x_increment = random.choice(start_directions)
        self.y_increment = random.choice(start_directions)
        self.move_speed = 0.08

    def move(self):
        current_xco = self.xcor()
        current_yco = self.ycor()
        self.setposition(current_xco + self.x_increment, current_yco + self.y_increment)

    def reverse_x(self):
        self.x_increment *= -1
        self.move_speed *= 0.8

    def reverse_y(self):
        self.y_increment *= -1

    def reset_ball(self):
        self.setposition(0, 0)
        self.move_speed = 0.08
        self.reverse_x()
        self.y_increment = random.choice(start_directions)
