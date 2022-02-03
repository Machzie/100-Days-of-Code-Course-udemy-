import turtle

SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def create_snake(self):
        for position in SNAKE_POSITIONS:
            self.add_body(position)

    def add_body(self, position):
        new_body = turtle.Turtle(shape='square')
        new_body.penup()
        new_body.color('white')
        new_body.fillcolor('green')
        new_body.setposition(position)
        self.snake_body.append(new_body)

    def extend(self):
        self.add_body(self.snake_body[-1].position())

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].setposition(self.snake_body[i - 1].position())
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
