import keyboard
import time
from tkinter import *




okienko = Tk()
canvas = Canvas(okienko,width=800,height=800,bg="#fd285a")
canvas.pack()


szerokosc=800
wysokosc=800
canvas.create_oval(50,50,szerokosc,wysokosc,fill="#28fdcb")
tablica =[]
while(True):
    if(keyboard.is_pressed("Up")):
        szerokosc=szerokosc-3
        wysokosc=wysokosc-3
        tablica.append(canvas.create_oval(50,50,szerokosc,wysokosc,fill="#28fdcb"))
    if(keyboard.is_pressed("Down")):
        canvas.delete(tablica[len(tablica)-1])
        tablica.pop(len(tablica)-1)


    okienko.update()
