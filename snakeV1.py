
from turtle import *
from random import *



class head(Turtle):
    def __init__(self):
        super().__init__()
        super().shape("square")
        super().color("green")
        super().penup()
        super().speed(0)
        super().goto(0,100)
        self.direction="in rest"

    def up(self):
        self.direction = "up"
    def down(self):
        self.direction = "down"
    def right(self):
        self.direction = "right"
    def left(self):
        self.direction = "left"


    def motion(self):
        if(self.direction == "up"):
            x = super().xcor()
            y = super().ycor() + 10
            super().goto(x,y)
        elif(self.direction == "down"):
            x = super().xcor()
            y = super().ycor() - 10
            super().goto(x,y)

        elif(self.direction == "left"):
            x = super().xcor() - 10
            y = super().ycor() 
            super().goto(x,y)

        elif(self.direction == "right"):
            x = super().xcor() + 10
            y = super().ycor() 
            super().goto(x,y)
        

class fruit(Turtle):
    def __init__(self):
        super().__init__()
        super().shape("circle")
        super().penup()

    def hit(self):
        x = randint(-250,250)
        y = randint(-250,250)
        super().goto(x,y)


class banan(fruit):
    def __init__(self):
        super().__init__()
        super().color("yellow")
        super().shapesize(0.5,2.0)

class orange(fruit):
    def __init__(self):
        super().__init__()
        super().color("orange")
        super().shapesize(0.5,0.5)

class apple(fruit):
    def __init__(self):
        super().__init__
        super().color("red")
        


banan = banan()
jablko = apple()
mandarynka = orange()
glowa = head()

def clockTick():
    glowa.motion()

    if(glowa.distance(banan)<15):
        banan.hit()

    if(glowa.distance(jablko)<15):
        jablko.hit()

    if(glowa.distance(mandarynka)<15):
        mandarynka.hit()

    ontimer(clockTick,20)

onkey(glowa.up,"w")

onkey(glowa.down,"s")

onkey(glowa.right,"d")

onkey(glowa.left,"a")

clockTick()

        
 
        
 
listen()
mainloop()


