from turtle import *
from random import *

colors= ["pink", "deep pink", "magenta", "purple"]
sr = Screen()
sr.tracer(0)
balls = []
for i in range(0,10):
    ball = Turtle()
    ball.color(colors[randint(0,3)])
    ball.shape("circle")
    ball.penup()
    ball.goto(randint(-300,300),200)
    ball.velY = uniform(-0.02,-0.01)
    ball.velX = 1
    ball.speed(0)
    balls.append(ball)

gravity = -0.01


while(True):
    sr.update()
    for ball in balls:
        y = ball.ycor()
        ball.velY= ball.velY + gravity
        ball.sety(y+ball.velY)

        x = ball.xcor()
        ball.setx(x+ ball.velX)
    
        if(ball.ycor()<-200):
            ball.velY = ball.velY*(-1)

        if(ball.xcor()<-200 or ball.xcor()>200 ):
            ball.velX = ball.velX*(-1)

        for ballB in balls:
            if(ball != ballB):
                if(ball.distance(ballB)<10):
                    ball.velX = ball.velX*(-1)
                    ballB.velX = ballB.velX*(-1)
                    ball.velY = ball.velY*(-1)
                    ballB.velY = ballB.velY*(-1)

sr.mainloop()
