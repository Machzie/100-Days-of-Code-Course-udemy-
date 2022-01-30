# Day 19 Project - Turtle Racing

import turtle
import random

is_race_on = False

screen = turtle.Screen()
screen.setup(width=500, height=400)

user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")

turtle1 = turtle.Turtle(shape="turtle")
turtle2 = turtle.Turtle(shape="turtle")
turtle3 = turtle.Turtle(shape="turtle")
turtle4 = turtle.Turtle(shape="turtle")
turtle5 = turtle.Turtle(shape="turtle")
turtle6 = turtle.Turtle(shape="turtle")
turtles_list = [turtle1, turtle2, turtle3, turtle4, turtle5, turtle6]
turtle_colours = ["red", "orange", "yellow", "green", "blue", "purple"]

y_position = -100
for i in range(0, len(turtles_list)):
    current_turtle = turtles_list[i]
    current_turtle.penup()
    current_turtle.color(turtle_colours[i])
    current_turtle.setposition(-230, y_position)
    y_position += 40

if user_input:
    is_race_on = True

while is_race_on:

    for turtle in turtles_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_input.lower():
                print(f"You win! The {winning_colour} turtle won")
            else:
                print(f"You lost. The {winning_colour} turtle won.")
        else:
            turtle.speed('slow')
            turtle.forward(random.randint(0, 10))

screen.exitonclick()
