from turtle import *

miasta = ["Paris","Munich","New York","Milano","Moscow","Kiev","Sydney","London","Tokio","Warsaw"]
coords=[-50,200,-200,-30,200,250,75,50,250,50,100,-50,75,-200,-100,-230,-250,-200,100]

penup()
for i in range(0,10):
    
    goto(coords[2*i],coords[2*i+1])
    pendown()
    write(miasta[i])
    penup()

input()