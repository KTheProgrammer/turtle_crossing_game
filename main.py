import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
spot = Player()
cars = CarManager()
scores = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(fun=spot.move_up, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # spot.finish()
    cars.make_car()
    cars.move_car()

    # Detect collision with car
    for car in cars.my_cars:
        if car.distance(spot) < 30:
            scores.game_over()
            game_is_on = False

    # Detect finish line
    if spot.ycor() >= 280:
        scores.new_level()
        spot.goto(0, -280)
        cars.speed_up()

screen.exitonclick()
