# Day 22 Project - Pong Game

import turtle
import paddle
import ball
import time
import scoreboard

EASY_BALL_SPEED = 0.1
HARD_BALL_SPEED = 0.05

screen = turtle.Screen()
screen.setup(800, 600, starty=20)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

left_paddle = paddle.Paddle((-350, 0))
right_paddle = paddle.Paddle((350, 0))
ball = ball.Ball()
scoreboard = scoreboard.Scoreboard()

screen.onkeypress(right_paddle.move_up, 'Up')
screen.onkeypress(right_paddle.move_down, 'Down')
screen.onkeypress(left_paddle.move_up, 'w')
screen.onkeypress(left_paddle.move_down, 's')
screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 279 or ball.ycor() < -279:
        ball.reverse_y()

    # Detect collision with paddles
    if (ball.xcor() > 330 and ball.distance(right_paddle) < 50) or (ball.xcor() < -330 and ball.distance(left_paddle) < 50):
        ball.reverse_x()
    # Detect ball going out of bounds
    elif ball.xcor() > 420:
        ball.reset_ball()
        scoreboard.increase_left_score()
    elif ball.xcor() < -420:
        ball.reset_ball()
        scoreboard.increase_right_score()

    if scoreboard.left_score == 10:
        scoreboard.left_wins()
        game_is_on = False
    elif scoreboard.right_score == 10:
        scoreboard.right_wins()
        game_is_on = False

screen.exitonclick()
