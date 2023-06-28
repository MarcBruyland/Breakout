from turtle import Turtle
from constants import WIDTH, HEIGHT, PADDING_SCOREBOARD, N_LIVES

FONT = ("Courier", 15, "normal")

print(WIDTH, HEIGHT)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.n_lives = N_LIVES
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-WIDTH / 2 + PADDING_SCOREBOARD, HEIGHT / 2 - PADDING_SCOREBOARD)
        if self.n_lives > 0:
            self.write(f"{self.n_lives} lives", align="left", font=FONT)
        else:
            self.write("GAME OVER", align="left", font=FONT)
        self.goto(WIDTH / 2 - PADDING_SCOREBOARD, HEIGHT / 2 - PADDING_SCOREBOARD)
        self.write(f"{self.score} points", align="right", font=FONT)

    def increase_score(self, points):
        self.score += points
        self.update_scoreboard()

    def decrease_n_lives(self):
        self.n_lives -= 1
        self.update_scoreboard()

