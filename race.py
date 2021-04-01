from turtle import *
from random import *

class sedzia(Turtle):
    def __init__ (self,x):
        super().__init__()
        super().penup()
        super().goto(x,-300)
        super().pendown()
        super().setheading(90)

    def drawLine(self):
        super().forward(600)



class sedziowie():
    def __init__(self):
        self.sedziowie = []
        for i in range(20):
            self.sedziowie.append(sedzia(-300+30*i))

    def rysujBoisko(self):
        for obiekt in self.sedziowie:
            obiekt.drawLine()





arbitrzy = sedziowie()
arbitrzy.sedziowie[0].pensize(3)
arbitrzy.sedziowie[19].pensize(3)
arbitrzy.rysujBoisko()

arbitrzy.sedziowie[0].write("START")
arbitrzy.sedziowie[19].write("META")

class zawodnik(Turtle):
    def __init__(self, y):
        super().__init__()
        super().penup()
        super().goto(-300,y)
        self.isWiner = False

    def run(self):
        super().forward(randint(0,10))
        aktualnaPozycja = super().xcor()
        if(aktualnaPozycja>300):
            super().write("WYGRALEM!")
            self.isWiner = True

class pelaton():
    def __init__(self):
        self.zawodnicy = []
        for i in range(10):
            self.zawodnicy.append(zawodnik(-200+40*i))

    def wyscig(self):
        for zawodnik in self.zawodnicy:
            zawodnik.run()

naszPelaton = pelaton()

while (True):
    naszPelaton.wyscig()


zawodnik1 = zawodnik(0)

while(True):
    zawodnik1.run()


exitonclick()
