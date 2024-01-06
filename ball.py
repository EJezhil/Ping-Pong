import time
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.show_ball()
        self.additionx = -10
        self.additiony = -10
    def show_ball(self):
        self.shape("circle")
        self.penup()
        self.speed(10)
        self.goto(0, 0)
        self.color("white")

    def move_ball(self):
        time.sleep(0.03)
        self.x = self.xcor() + self.additionx
        self.y = self.ycor() + self.additiony
        self.goto(self.x , self.y)