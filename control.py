from turtle import *
from pyglet.window import key



class gracz(Turtle):
    def __init__(self):
        super().__init__()
        super().shape("turtle")
        super().penup()

    def goUp(self):
        y = super().ycor() + 10
        super().sety(y)

    def goDown(self):
        y = super().ycor() - 10
        super().sety(y)

    def goRight(self):
        x = super().xcor() + 10
        super().setx(x)

    def goLeft(self):
        x = super().xcor() - 10
        super().setx(x)

    def goUpRight(self):
        x = super().xcor() + 10
        y = super().ycor() + 10
        super().goto(x,y)



    def drawCircle(self):
        super().pendown()
        for i in range(36):
            super().forward(2)
            super().left(10)
        super().penup()

bgcolor("lime")
gracz1 = gracz()


onkey(gracz1.goUp,"w") #UP
onkey(gracz1.goDown, "s") #
onkey(gracz1.goRight,"d")
onkey(gracz1.goLeft,"a")
onkey(gracz1.drawCircle,"k")
onkey(gracz1.goUpRight,"e")


#space
#SPACE

listen()
mainloop()
