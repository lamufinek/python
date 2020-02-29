from tkinter import *
import time
import keyboard
import random

okienko = Tk()
kanwas = Canvas(okienko, width = 400, height =400)
kanwas.pack()




class Ball():
    def __init__(self,kanwas, promien, pozycjaX, pozycjaY, kolor):
        self.id = kanwas.create_oval(pozycjaX,pozycjaY,pozycjaX+promien,pozycjaY+promien, fill = kolor)
        self.pozycjaX = pozycjaX+promien/2
        self.pozycjaY = pozycjaY+promien/2
        self.kanwas = kanwas

    def motionUp(self):
        self.kanwas.move(self.id,0,-1)
        self.pozycjaY= self.pozycjaY - 1

    def motionDown(self):
        self.kanwas.move(self.id,0,1)
        self.pozycjaY= self.pozycjaY + 1
    def motionRight(self):
        self.kanwas.move(self.id,1,0)
        self.pozycjaX= self.pozycjaX + 1
    def motionLeft(self):
        self.kanwas.move(self.id,-1,0)
        self.pozycjaX= self.pozycjaX - 1

    def Control(self):
        if(keyboard.is_pressed("Up")):
            self.motionUp()
        if(keyboard.is_pressed("Down")):
            self.motionDown()
        if(keyboard.is_pressed("Right")):
            self.motionRight()
        if(keyboard.is_pressed("Left")):
            self.motionLeft()

class Item():
    def __init__(self, kanwas, promien, pozycjaX, pozycjaY, kolor):
        self.id = Ball(kanwas, promien, pozycjaX+promien, pozycjaY+promien, kolor)
        self.pozycjaX = pozycjaX
        self.pozycjaY = pozycjaY
        self.canvas = kanwas

    def distanceControll(self,pozycjaX,pozycjaY):
        if(abs(self.pozycjaX-pozycjaX)<=20 and abs(self.pozycjaY-pozycjaY)<=20 ):
            self.canvas.delete(self.id.id)




kulka1 = Ball(kanwas, 40 , 50, 50, "red")
tablicaItem = []
for i in range(0,56):
    item = Item(kanwas, 5, random.randint(20,380), random.randint(20,380), "pink")
    tablicaItem.append(item)


while(True):
    time.sleep(0.01)
    kulka1.Control()
    for i in tablicaItem:
        i.distanceControll(kulka1.pozycjaX, kulka1.pozycjaY)
    okienko.update()
    if(keyboard.is_pressed("q")):
        break
