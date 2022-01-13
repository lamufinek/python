from turtle import *
from random import *



class head(Turtle):
    def __init__(self):
        super().__init__()
        super().shape("square")
        super().color("green")
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
        if(self.direction=="up"):
            y = super().ycor()
            super().sety(y + 20)
        elif(self.direction=="down"):
            y = super().ycor()
            super().sety(y - 20)
        elif(self.direction=="right"):
            x = super().xcor()
            super().setx(x + 20)
        elif(self.direction=="left"):
            x = super().xcor()
            super().setx(x - 20)



class segment(Turtle):
    def __init__(self,x,y):
        super().__init__()
        super().shape("square")
        super().color("red")
        super().penup()
        super().speed(0)
        super().shapesize(0.8,0.8)
        super().goto(x,y)

    def motion(self,x,y):
        super().goto(x,y)

class body():
    def __init__(self):
        self.segments = []
        self.Xcoords = []
        self.Ycoords = []

    def enlarge(self,segment):
        pass

    def update(self):
        for i in range(len(self.segments)-1, 0, -1 ):
            self.Xcoords[i] = self.Xcoords[i-1]
            self.Ycoords[i] = self.Ycoords[i-1]
            x = self.Xcoords[i]
            y = self.Ycoords[i]
            self.segments[i].motion(x,y)

        self.Xcoords[0] = self.segments[0].xcor()
        self.Ycoords[0] = self.segments[0].ycor()

    def lastX(self):
        return self.Xcoords[len(self.Xcoords)-1]

    def lastY(self):
        return self.Ycoords[len(self.Ycoords)-1]



class fruit(Turtle):
    def __init__(self,body):
        super().__init__()
        super().shape("circle")
        super().color("orange")
        super().penup()
        super().speed(0)
        super().shapesize(0.5,0.5)
        super().goto(0,0)
        self.body = body

    def hit(self):
        xTail = self.body.lastX()
        yTail = self.body.lastY()
        self.body.enlarge(segment(xTail,yTail))
        x = randint(-250,250)
        y = randint(-250,250)
        super().goto(x,y)

glowa = head()
cialo = body()
cialo.enlarge(glowa)
owoc = fruit(cialo)


def clockTick():
    ##################################################
    glowa.motion()
    
    ##################################################
    ontimer(clockTick,20)



########################################################
clockTick()
onkey(glowa.up,"w")
onkey(glowa.down,"s")
onkey(glowa.right,"d")
onkey(glowa.left,"a")

########################################################
listen()
mainloop()
