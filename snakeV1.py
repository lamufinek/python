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
        
        
 

glowa = head()

onkey(glowa.up,"w")

onkey(glowa.down,"s")

onkey(glowa.right,"d")

onkey(glowa.left,"a")
        
        
 
        
 
listen()
mainloop()
