from turtle import *



color("red")
goto(-300,0)
goto(300,0)
goto(0,0)

shape("circle")
color("orange")


ACCy = -1
Vy = 20
Vx = 15
t = 0
tdelta =0.25
tlumienie = Vy

while(True):
    x = -300 + Vx*t #s=v*t
    Vy = Vy + ACCy * tdelta
    y = Vy*t #s=v*t
    goto(x,y)
    t = t + tdelta
    if(ycor())<-5:
        Vy = tlumienie / 6
        tlumienie = tlumienie - 1
