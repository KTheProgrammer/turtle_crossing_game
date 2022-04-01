from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(-230, 260)
        self.scored = 1
        self.write(f"Level: {self.scored}", align="center", font=FONT)

    def new_level(self):
        self.scored += 1
        self.clear()
        self.write(f"Level: {self.scored}", align="center", font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
