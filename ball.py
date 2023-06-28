from turtle import Turtle
from constants import WIDTH, HEIGHT, PADDING_PADDLE

INITIAL_SPEED = 0.1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.step_x = 10
        self.step_y = 10
        self.move_speed = INITIAL_SPEED
        self.reset_position()

    def move(self):
        new_x = self.xcor() + self.step_x
        new_y = self.ycor() + self.step_y
        self.goto(new_x, new_y)

    def bounce_on_left_wall(self):
        self.step_x *= -1

    def bounce_on_right_wall(self):
        self.step_x *= -1

    def bounce_on_upper_wall(self):
        self.step_y *= -1

    def bounce_on_brick(self):
        self.step_y *= -1

    def bounce_on_paddle(self):
        self.step_y *= -1

    def reset_position(self):
        # self.step_x *= -1
        # self.home()
        # self.move_speed = INITIAL_SPEED
        self.step_x = 10
        self.step_y = 10
        self.penup()
        self.hideturtle()
        self.goto(0, -HEIGHT/2 + PADDING_PADDLE + 50)
        self.showturtle()


