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
        self.rozmiar = 1
        self.canBeEaten = True
        self.body.speed(1000)

    def move(self):
        x = randint(-30,30)
        y = randint(-30,30)
        X = self.body.xcor() + x
        Y = self.body.ycor() + y
        self.body.goto(X,Y)

    def fight(self, enemy):
        if(self.rozmiar == enemy.rozmiar):
            losowanie = randint(1,2)
            if(losowanie == 1):
                self.rozmiar = self.rozmiar + 1
                self.body.shapesize(self.rozmiar)
                enemy.body.reset()
                enemy.canBeEaten = False
            else:
                enemy.rozmiar = enemy.rozmiar + 1
                enemy.body.shapesize(enemy.rozmiar)
                self.body.reset()
                self.canBeEaten = False
        elif(self.rozmiar > enemy.rozmiar):
            self.rozmiar = self.rozmiar + 1
            self.body.shapesize(self.rozmiar)
            enemy.body.reset()
            enemy.canBeEaten = False
        
        elif(self.rozmiar < enemy.rozmiar):
            enemy.rozmiar = enemy.rozmiar + 1
            enemy.body.shapesize(enemy.rozmiar)
            self.body.reset()
            self.canBeEaten = False





turtles = []
for i in range(0,50):
    turtle = ourTurtle()
    turtles.append(turtle)

while(True):
    for each in turtles:
        each.move()
        for eachOne in turtles:
            if(eachOne != each):
                if(eachOne.canBeEaten == True and each.canBeEaten == True):
                    if(each.body.distance(eachOne.body)<20):
                        each.fight(eachOne)





