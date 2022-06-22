from turtle import *


player1 = Turtle()
player1.shape("turtle")
player1.penup()
player1.color("red")
player1.goto(100,100)
player1.shapesize(2.0)

player2 = Turtle()
player2.shape("turtle")
player2.penup()
player2.color("blue")
player2.goto(-100,-100)



fruit = Turtle()
fruit.shape("circle")
fruit.color("orange")
fruit.shapesize(0.5)

def p1Up():
    player1.setheading(90)
    player1.forward(1)

def p1Down():
    player1.setheading(-90)
    player1.forward(1)


def p1Right():
    player1.setheading(0)
    player1.forward(1)

def p1Left():
    player1.setheading(180)
    player1.forward(1)


onkeypress(p1Up,"w")
onkeypress(p1Down,"s")
onkeypress(p1Right,"d")
onkeypress(p1Left,"a")


listen()
mainloop()




