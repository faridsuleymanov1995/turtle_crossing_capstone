from turtle import Turtle
import random
YCOR = [i for i in range(-240, 280, 40)]
COLORS = ['red', 'yellow', 'black', 'blue', 'orange']

class Obstacle():
    def __init__(self):
        self.list1 = []

    def create(self):
        obst = Turtle()
        obst.penup()
        obst.shape('square')
        obst.color(random.choice(COLORS))
        obst.turtlesize(stretch_wid=0.5, stretch_len=2)
        obst.goto(300, random.choice(YCOR))
        self.list1.append(obst)

    def move1(self):
        for i in self.list1:
            i.setx(i.xcor() - 10)

