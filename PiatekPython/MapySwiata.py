from turtle import *

miasta = ["Paris","Munich","New York","Milano","Moscow","Kiev","Sydney","London","Tokio","Warsaw"]
coords=[-50,200,-200,-30,200,250,75,50,250,50,100,-50,75,-200,-100,-230,-250,-200,100,200]

penup()
for i in range(0,10):
    
    goto(coords[2*i],coords[2*i+1])
    pendown()
    write(miasta[i])
    penup()





class Miasto():
    def __init__(self,nazwa,x,y):
        self.nazwa = nazwa
        self.x = x
        self.y = y
        self.connections = []

    def addConnection(self,name):
        self.connections.append(name)


Miasta = []
coonections = [
    [0,1,0,0,0,0,1,0,0,0],
    [1,0,0,1,0,0,0,1,0,1],
    [0,0,0,0,1,0,0,0,0,0],
    [0,1,0,0,0,1,0,0,0,0],
    [0,0,1,0,0,1,0,0,0,0],
    [0,0,0,1,1,0,1,0,0,0],
    [1,0,0,0,0,1,0,0,0,0],
    [0,1,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,1,0,0],
    [0,1,0,0,0,0,0,0,0,0],
]

for i in range(0,10):
    
    
    Miasta.append(Miasto(miasta[i],coords[2*i],coords[2*i+1]))


for i in range(0,10):
    Miasta[i]
    for j in range(0,10):
        if(coonections[i][j]==1):
            Miasta[i].addConnection(miasta[j])



print(Miasta[2].connections)
print(Miasta[3].connections)


class Mapa():
    def __init__(self,miasta):
        self.miasta = miasta

    def findConnection(self, miejsce1, miejsce2):
        mozliweTrasy = []
        trasa = []

        for each in self.miasta:
            if each.name == miejsce1:
                miasto1 = each
            if each.name == miejsce2:
                miasto2 = each

        for each in miasto1.connections:
            trasa.append(miasto1.name)
            trasa.append(each)
            mozliweTrasy.append(trasa)     



    
