#  Press W S fo Up and Down for Left Paddle
#  Press up and down Arrow key for Up and down for Right Paddle


import time
from turtle import Turtle, Screen

from ball import Ball
from paddle import Paddle
from score import Score

start = True
position_of_right_paddle = (560, 100)
position_of_left_paddle = (-560, -240)

screen = Screen()
screen.setup(1200, 800)
screen.listen()
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)


def show_line():
    x = 0
    y = 300
    for i in range(0, 13):
        a = Turtle()
        a.penup()
        a.write("|", False, "center", font=('Arial', 20, 'normal'))
        a.color("white")
        a.goto(x, y)
        y -= 60


score = Score()

paddle_left = Paddle()
paddle_left.show_paddle(position_of_left_paddle)
paddle_right = Paddle()
paddle_right.show_paddle(position_of_right_paddle)

ball = Ball()
show_line()

screen.onkeypress(fun=paddle_left.left_up, key="w")
screen.onkeypress(fun=paddle_left.left_down, key="s")
screen.onkeypress(fun=paddle_right.right_up, key="Up")
screen.onkeypress(fun=paddle_right.right_down, key="Down")

while start:
    paddle_left.restricting_limit()
    ball.move_ball()
    score.reset_score()
    print(f"{ball.xcor()},{ball.ycor()}")

    if ball.xcor() > 600:
        Score.LEFT_SCORE += 1
        ball.goto(0, 0)

    elif ball.xcor() < -600:
        Score.RIGHT_SCORE += 1
        ball.goto(0, 0)

    elif ball.xcor() > 0 and ball.ycor() > 340:
        ball.additiony *= -1

    elif ball.xcor() > 0 and ball.ycor() < - 340:
        ball.additiony *= -1

    elif ball.xcor() < -0 and ball.ycor() < - 340:
        ball.additiony *= -1

    elif ball.xcor() < -0 and ball.ycor() > 340:
        ball.additiony *= -1

    if ball.distance(Paddle.paddles[0]) < 40 and ball.xcor() < -520:
        print(f"distance{Paddle.paddles[0]}")
        ball.additionx *= -1

    if ball.distance(Paddle.paddles[1]) < 40 and ball.xcor() > 520:
        ball.additionx *= -1

    screen.update()

screen.exitonclick()
