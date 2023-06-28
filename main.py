from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from wall import Wall
from scoreboard import Scoreboard
from constants import WIDTH, HEIGHT, PADDING_PADDLE
import time

# WIDTH = 1000
# HEIGHT = 500

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Breakout game")
# screen.tracer(0)

paddle = Paddle((0, -HEIGHT/2 + PADDING_PADDLE))
scoreboard = Scoreboard()
wall = Wall()
ball = Ball()


screen.listen(xdummy=None, ydummy=None)
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with paddle
    if ball.ycor() < -HEIGHT / 2 + PADDING_PADDLE + 20 and ball.distance(paddle) < 50:
        ball.bounce_on_paddle()

    # detect collision with upper_wall
    if ball.ycor() > (HEIGHT / 2) - 20:
        ball.bounce_on_upper_wall()

    # detect collision with left_wall
    if ball.xcor() < (-WIDTH / 2) + 20:
        ball.bounce_on_left_wall()

    # detect collision with right_wall
    if ball.xcor() > (WIDTH / 2) - 20:
        ball.bounce_on_right_wall()

    # detect ball goes out
    if ball.ycor() < -HEIGHT / 2:
        scoreboard.decrease_n_lives()
        if scoreboard.n_lives > 0:
            ball.reset_position()
        else:
            game_is_on = False

    # detect collision with  wall
    for brick in wall.lst_of_bricks:
        if ball.distance(brick) < 50:
            ball.bounce_on_brick()
            wall.lst_of_bricks.remove(brick)
            brick.hideturtle()
            scoreboard.increase_score(brick.points)
            break

    screen.update()


screen.exitonclick()
