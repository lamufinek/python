from turtle import *
from random import *

sr = Screen()
sr.tracer(0)
ball = Turtle()
ball.shape("circle")
ball.penup()
ball.goto(0,200)
ball.velY = -2
ball.velX = 2

gravity = -0.1


while(True):
    sr.update()
    y = ball.ycor()
    ball.velY= ball.velY + gravity
    ball.sety(y+ball.velY)

    x = ball.xcor()
    ball.setx(x+ ball.velX)
    
    if(ball.ycor()<-200):
        ball.velY = ball.velY*(-1)

    if(ball.xcor()<-200 or ball.xcor()>200 ):
        ball.velX = ball.velX*(-1)

    
input()