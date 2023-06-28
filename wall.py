from turtle import Turtle
from constants import WIDTH, SPACE_BETWEEN_BRICKS, BRICKS_PER_ROW


class Brick(Turtle):
    def __init__(self, color, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=(WIDTH/BRICKS_PER_ROW-SPACE_BETWEEN_BRICKS)/20)    # 1 unit is 20 pixels
        self.alive = True
        self.points = 0
        if color == "yellow":
            self.points = 1
        elif color == "green":
            self.points = 3
        elif color == "orange":
            self.points = 5
        elif color == "red":
            self.points = 7
        self.goto(position)
        self.showturtle()


class Wall():
    def __init__(self):
        self.lst_of_bricks = []
        self.make_wall()

    def make_wall(self):
        self.add_wall_row("yellow", -25)
        self.add_wall_row("yellow", 0)
        self.add_wall_row("green", 25)
        self.add_wall_row("green", 50)
        self.add_wall_row("orange", 75)
        self.add_wall_row("orange", 100)
        self.add_wall_row("red", 125)
        self.add_wall_row("red", 150)

    def add_wall_row(self, color, row_height):
        for i in range(BRICKS_PER_ROW):
            brick_space = WIDTH / BRICKS_PER_ROW
            self.lst_of_bricks.append(Brick(color, (-WIDTH/2 + (i+0.5) * brick_space, row_height)))
