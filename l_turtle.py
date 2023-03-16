from turtle import Turtle

class L_turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('green')
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def start(self):
        self.goto(0, -280)

    def moveup(self):
        self.goto(0, self.ycor() + 10)

    def movedown(self):
        self.goto(0, self.ycor() - 10)

