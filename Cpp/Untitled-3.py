from random import *

tablicaLiczb = []

for y in range(0,100):
    a = randint(0,10000)
    tablicaLiczb.append(a)


i= 0 
while(i<len(tablicaLiczb)-1):
    if(tablicaLiczb[i]>tablicaLiczb[i+1]):
        temp = tablicaLiczb[i]
        tablicaLiczb[i] = tablicaLiczb[i+1]
        tablicaLiczb[i+1] = temp
        i = 0
    i = i+1




print(tablicaLiczb)