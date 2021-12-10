from turtle import *
from random import *


class ourTurtle():
    def __init__(self):
        self.body = Turtle()
        self.body.penup()
        self.body.shape("turtle")
        self.body.color("green")
        x = randint(-300,300)
        y = randint(-300,300)
        self.body.goto(x,y)

    def move(self):
        x = randint(-10,10)
        y = randint(-10,10)
        X = self.body.xcor() + x
        Y = self.body.ycor() + y
        self.body.goto(X,Y)

turtles = []
for i in range(0,10):
    turtle = ourTurtle()
    turtles.append(turtle)

while(True):
    for each in turtles:
        each.move() 





