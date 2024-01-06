from turtle import Turtle

class Paddle():
    paddles = []

    def __init__(self):
        self.x = 90
        self.y = 270

    def show_paddle(self, position):
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.shape("square")
        self.paddle.speed(0)
        self.paddle.goto(position)
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=4, stretch_len=1)
        self.paddles.append(self.paddle)

    def left_up(self):
        posx = self.paddles[0].xcor()
        posy = self.paddles[0].ycor()
        self.paddles[0].goto(posx, posy + 40)

    def left_down(self):
        posx = self.paddles[0].xcor()
        posy = self.paddles[0].ycor()
        self.paddles[0].goto(posx, posy - 40)

    def right_up(self):
        posx = self.paddles[1].xcor()
        posy = self.paddles[1].ycor()
        self.paddles[1].goto(posx, posy + 40)

    def right_down(self):
        posx = self.paddles[1].xcor()
        posy = self.paddles[1].ycor()
        self.paddles[1].goto(posx, posy - 40)

    def restricting_limit(self):
        if self.paddles[0].ycor() > 360.0:
            self.paddles[0].goto(-560,360)

        if self.paddles[0].ycor() < -340.0:
            self.paddles[0].goto(-560,-340)

        if self.paddles[1].ycor() > 360.0:
            self.paddles[1].goto(560, 360)

        if self.paddles[1].ycor() < -360.0:
            self.paddles[1].goto(560, -360)
