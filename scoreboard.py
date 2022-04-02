from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 260)
        self.scored = 1
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.update()

    def new_level(self):
        self.scored += 1
        self.clear()
        self.write(f"Level: {self.scored} Highest Level: {self.high_score}", align="center", font=FONT)

    def update(self):
        self.clear()
        self.write(f"Level: {self.scored} Highest Level: {self.high_score}", align="center", font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)

    def set_high_score(self):
        if self.scored > self.high_score:
            self.high_score = self.scored
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
                self.update()
