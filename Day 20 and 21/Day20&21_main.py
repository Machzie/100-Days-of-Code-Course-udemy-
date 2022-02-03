# Day 20 and 21 Project - Snake Game

import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Set up screen
screen = turtle.Screen()
screen.setup(560, 560)
screen.title('My Snake Game')
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    # Move the snake
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 10:
        food.refresh()
        scoreboard.clear()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.snake_head.xcor() > 279 or snake.snake_head.xcor() < -279 or \
            snake.snake_head.ycor() > 279 or snake.snake_head.ycor() < -279:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with tail
    for body_part in snake.snake_body[1:]:
        if snake.snake_head.distance(body_part) < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
