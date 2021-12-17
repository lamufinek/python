from turtle import *
from random import *


class ourTurtle():
    def __init__(self, kat):
        self.kat = kat
        self.body = Turtle()
        self.body.color("white")
        self.body.speed(1000)
        self.liczba = int(abs(360/kat))



    def wykreslWzor(self):
        x = randint(-300,300)
        y = randint(-300,300)
        self.body.penup()
        self.body.goto(x,y)
        self.body.pendown()
        for i in range(0, self.liczba): 
            self.body.left(self.kat)
            self.body.forward(5)




tablica = []
for i in range(0,20):
    box = randint(80,120)
    zlow = ourTurtle(30)
    tablica.append(zlow)


bgcolor("black")

for i in range(20):
    for each in tablica:
        each.wykreslWzor()






        




    




