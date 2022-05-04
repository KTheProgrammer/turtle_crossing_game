from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "brown"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.my_cars = []
        self.speedy = STARTING_MOVE_DISTANCE

    def make_car(self):
        random_create_car = random.randint(1, 6)
        if random_create_car == 6:
            car = Turtle(shape="square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=3)
            car.x = 10
            car.y = random.randint(-230, 230)
            car.goto(300, car.y)
            self.my_cars.append(car)

    def move_car(self):
        for car in self.my_cars:
            car.backward(self.speedy)

    def speed_up(self):
        self.speedy += MOVE_INCREMENT
