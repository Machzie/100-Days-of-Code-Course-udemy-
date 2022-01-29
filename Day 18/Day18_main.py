# Day 18 Challenge - The Hirst Painting

# colorgram python package allows you to extract colours from images
import colorgram
import turtle
import random

colours = colorgram.extract('damien-hirst-lactulose.jpg', 15)

rgb_colour_list = []
for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    # don't include the background colour (any colour close to white)
    if r + g + b < 700:
        rgb_colour_list.append((r, g, b))

tortue = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)
screen.setworldcoordinates(-210, -210, 210, 210)


def step_size(n_dots_per_row):
    """returns the distance between dots, based on the number of dots required"""
    return 400//n_dots_per_row


def draw_row(n_dots):
    """draws a row of dots on the graphics screen"""
    for i in range(n_dots):
        tortue.dot(20, random.choice(rgb_colour_list))
        tortue.penup()
        tortue.forward(step_size(n_dots))
    tortue.dot(20, random.choice(rgb_colour_list))


tortue.speed('fast')

# Set the number of dots per row / column
num_dots = 10

tortue.penup()
tortue.setposition(-200, -200)
y_position = tortue.position()[1]
for i in range(num_dots+1):
    tortue.setposition(-200, y_position)
    draw_row(num_dots)
    y_position += step_size(num_dots)


screen.exitonclick()
