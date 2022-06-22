from random import *
from turtle import *



pozycje = []

for i in range(-250,250,10):
    pozycje.append(i)



class Circle():
    def __init__(self, size, x, y):
        self.size = size
        self.x = x
        self.y = y
        self.body = Turtle()
        self.body.shape("circle")
        self.body.penup()
        self.body.speed(1000)

        self.body.goto(x,y)
        self.body.shapesize(size*3,size)
        self.body.speed(1)

kulki = []
for position in pozycje:
    size = uniform(0.1, 0.5)
    obiekt = Circle(size, position, 0)
    kulki.append(obiekt)


i= 0 
while(i<len(kulki)-1):
    if(kulki[i].size>kulki[i+1].size):
        temp = kulki[i].body.xcor()
        kulki[i].body.goto(kulki[i+1].body.xcor(),0) 
        kulki[i+1].body.goto(temp,0)
        newKulki = []
        temp = kulki[i]
        kulki[i]=kulki[i+1]
        kulki[i+1]=temp
    
        i = -1
    i = i+1
input()