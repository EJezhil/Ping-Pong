import time
from random import choice
from turtle import Turtle
from score import Score

MOVE = 20
POS = ()
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.x = self.xcor()
        self.y = self.ycor()
        self.show_ball()
        self.rand_pos = [(20, 20), (10, 20), (20, 10), (10, 10)]
        self.addx = self.x + self.MOVE
        self.subx = self.x - self.MOVE
        self.addy = self.y + self.MOVE
        self.suby = self.y - self.MOVE

        self.addadd = (self.addx, self.addy)
        self.addsub = (self.addx, self.suby)
        self.subsub = (self.subx, self.suby)
        self.subadd = (self.subx, self.addy)

    def show_ball(self):
        self.shape("square")
        self.penup()
        self.goto(0, 0)
        self.color("white")

    def move_ball(self):
        self.POS = self.addadd
        self.goto(self.POS)
        self.MOVE+=20
        # print(self.xcor())
        # print(self.ycor())
        if self.xcor() > 600:
            Score.LEFT_SCORE += 1
            self.goto(0, 0)

        elif self.xcor() < -600:
            Score.RIGHT_SCORE += 1
            self.goto(0, 0)

        elif self.xcor()> 0 and self.ycor() > 380:
            self.x = self.xcor()
            self.y = self.ycor()
            self.goto(self.x+self.MOVE,self.y-self.MOVE)

        elif self.xcor()> 0 and self.ycor() < -380:
            self.x = self.xcor()
            self.y = self.ycor()
            self.goto(self.x+self.MOVE,self.y+self.MOVE)

        elif self.xcor() < - 0 and self.ycor() < -380:
            self.x = self.xcor()
            self.y = self.ycor()
            self.goto(self.x-self.MOVE,self.y+self.MOVE)

        elif self.xcor() < -0  and self.ycor() >380:
            self.x = self.xcor()
            self.y = self.ycor()
            self.goto(self.x-self.MOVE,self.y-self.MOVE)

