from turtle import *


def kwadrat1():
    for x in range(0,4):
        forward(100)
        left(90)


def kwadrat2(rozmiar):
    for x in range(0,4):
        forward(rozmiar)
        left(90)


def kwadrat3(rozmiar,kolor):
    color(kolor)
    for x in range(0,4):
        forward(rozmiar)
        left(90)
    color("black")


def kwadrat4(rozmiar,kolor,x,y):
    penup()
    goto(x,y)
    pendown()
    color(kolor)
    for x in range(0,4):
        forward(rozmiar)
        left(90)
    color("black")



size = 50
speed(1000)
for coordY in range(-300,300,size*2):
    for coordX in range(int(-300-(size/2)),int(300-(size/2)),size):
        kwadrat4(size,"green",coordX,coordY)
    for coordX in range(-300,300,size):
        kwadrat4(size,"green",coordX,coordY+size)


input()



