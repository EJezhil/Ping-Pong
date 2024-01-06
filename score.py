from turtle import Turtle
class Score(Turtle):
    LEFT_SCORE = 0
    RIGHT_SCORE = 0

    def __init__(self):
        super().__init__()
        self.position_of_score = ((-100, 350), (100, 350))
        self.show_score()

    def show_score(self):
        for i in self.position_of_score:
            self.hideturtle()
            self.penup()
            self.write(f"{self.LEFT_SCORE}", font=('Arial', 30, 'normal'))
            self.goto(i)
            self.write(f"{self.RIGHT_SCORE}", font=('Arial', 30, 'normal'))
            self.color("white")

    def reset_score(self):
        self.reset()
        self.clear()
        self.show_score()
