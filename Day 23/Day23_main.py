# Day 23 Project - Turtle Crossing Game

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600, starty=20)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.onkey(player.move_player, 'Up')
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.new_car()
    cars.move_car()

    # Detect collision with car
    for car in cars.all_cars:
        if player.distance(car) < 20:
            print("Game over")
            game_is_on = False
            scoreboard.game_over()

    # Detect player getting to other side
    if player.ycor() == 280:
        player.reset_player()
        cars.increase_speed()
        scoreboard.increase_score()

screen.exitonclick()
