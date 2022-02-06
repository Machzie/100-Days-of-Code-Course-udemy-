from turtle import Turtle

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
EASY_MOVE_DISTANCE = 20
HARD_MOVE_DISTANCE = 10


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.setposition(pos)

    def move_up(self):
        current_xco = self.xcor()
        current_yco = self.ycor()
        self.setposition(current_xco, current_yco + EASY_MOVE_DISTANCE)

    def move_down(self):
        current_xco = self.xcor()
        current_yco = self.ycor()
        self.setposition(current_xco, current_yco - EASY_MOVE_DISTANCE)
