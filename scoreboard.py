from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.level = 0
        self.speed1 = 0.1
        self.refresh()

    def refresh(self):
        self.clear()
        self.level += 1
        self.goto(-260, 260)
        self.write(f'level: {self.level}',  font=('center', 20, 'normal'))
        self.speed1 *= 0.8

    def gameover(self):
        self.goto(0, 0)
        self.write(f'GAMEOVER', font=('center', 20, 'normal'))