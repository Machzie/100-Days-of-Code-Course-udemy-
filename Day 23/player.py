from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.reset_player()

    def move_player(self):
        self.forward(MOVE_DISTANCE)

    def reset_player(self):
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.setposition(STARTING_POSITION)
