from turtle import Screen
from l_turtle import L_turtle
from obstacle import Obstacle
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = L_turtle()
barrier = Obstacle()
score = Scoreboard()
screen.listen()
screen.onkeypress(fun=player.moveup, key='Up')
screen.onkeypress(fun=player.movedown, key='Down')
x = 3
list1 = []
end = True
while end:
    time.sleep(score.speed1)
    screen.update()

    if x % 3 == 0:
        barrier.create()
    barrier.move1()
    # it checks turtle colliding with obstacles
    for i in barrier.list1:
        if i.distance(player) < 20:
            score.gameover()
            end = False
    # whenever turtle pass it return turtle starting point and increase level
    if player.ycor() > 270:
        score.refresh()
        player.start()
    x += 1


screen.exitonclick()