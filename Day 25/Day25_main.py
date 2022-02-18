# Day 25 Project - USA States Game

import pandas
import turtle

screen = turtle.Screen()
screen.title("USA States Game")
screen.setup(750, 500)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states guessed", prompt="Please guess a state")
    if answer_state.title() in ("Exit", "Quit", "Close"):
        break
    for state in states_list:
        if answer_state.title() == state:
            guessed_states.append(state)
            row = states_data[states_data.state == state]
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(row.x), int(row.y))
            t.write(state, align="center")
            states_list.remove(state)

with open("states_to_learn.txt", "w") as to_learn:
    for state in states_list:
        to_learn.write(f"{state}\n")

# screen.exitonclick()
