from random import *
from turtle import *



xd = []
for i in range(10000000):
    pudeleczko = Turtle()
    pudeleczko.goto(randint(-200,200),randint(-200,200))
    xd.append(pudeleczko)

for i in range(10):
    for each in xd:
        each.forward(10)