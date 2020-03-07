import keyboard
import time
import random
from tkinter import *

def losowanieKoloruRGB():
    Red = random.randint(0,255)
    Green = random.randint(0,255)
    Blue = random.randint(0,255)
    Kolor = (Red, Green, Blue)
    print(Kolor)
    return Kolor

def RGBtoHex(kolorRGB):
    return "#"+'%02x%02x%02x' % kolorRGB

def losowanie():
    kolor=RGBtoHex(losowanieKoloruRGB())
    return kolor

def losowanieParametrow():
    x1=random.randint(0,800)
    y1=random.randint(0,800)
    srednica = random.randint(0,100)
    x2=x1+srednica
    y2=y1+srednica
    coords = (x1,y1,x2,y2)
    return coords



okienko = Tk()
canvas = Canvas(okienko, width=800, height=800, bg=losowanie())
canvas.pack()
for i in range(1,1000):
    canvas.create_oval(losowanieParametrow(),fill=losowanie())
    canvas.create_rectangle(losowanieParametrow(),fill=losowanie())
    canvas.create_arc(losowanieParametrow(),fill=losowanie())






while(True):
    okienko.update()
