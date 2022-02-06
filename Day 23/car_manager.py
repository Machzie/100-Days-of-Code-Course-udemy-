from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
Y_COORDS = list(range(-240, 240, 20))
X_COORD = 310


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def new_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            car_n = Turtle('square')
            car_n.shape('square')
            car_n.shapesize(stretch_len=2)
            car_n.penup()
            car_n.color(random.choice(COLORS))
            car_n.setposition(X_COORD, random.choice(Y_COORDS))
            self.all_cars.append(car_n)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
