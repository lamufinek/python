from tkinter import *
import time
import keyboard

okienko = Tk()
kanwas = Canvas(okienko, width = 400, height =400)
kanwas.pack()




class Ball():
    def __init__(self,kanwas, promien, pozycjaX, pozycjaY, kolor):
        self.id = kanwas.create_oval(pozycjaX,pozycjaY,pozycjaX+promien,pozycjaY+promien, fill = kolor)
        self.pozycjaX = pozycjaX
        self.pozycjaY = pozycjaY
        self.kanwas = kanwas

    def motionUp(self):
        self.kanwas.move(self.id,0,-1)

    def motionDown(self):
        self.kanwas.move(self.id,0,1)

    def motionRight(self):
        self.kanwas.move(self.id,1,0)

    def motionLeft(self):
        self.kanwas.move(self.id,-1,0)

    def Control(self):
        if(keyboard.is_pressed("Up")):
            self.motionUp()
        if(keyboard.is_pressed("Down")):
            self.motionDown()
        if(keyboard.is_pressed("Right")):
            self.motionRight()
        if(keyboard.is_pressed("Left")):
            self.motionLeft()




kulka1 = Ball(kanwas, 40 , 50, 50, "red")
kulka2 = Ball(kanwas, 70, 100, 100, "green")
kulka3 = Ball(kanwas, 100, 150, 150, "pink")


while(True):
    time.sleep(0.01)
    kulka1.Control()
    kulka2.Control()
    okienko.update()
    if(keyboard.is_pressed("q")):
        break
