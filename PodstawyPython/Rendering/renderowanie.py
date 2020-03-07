import keyboard
import time
from tkinter import *

okienko = Tk()
canvas = Canvas(okienko, width = 500, height = 500,bg="blue")
promien = 200
canvas.pack()

kulka = canvas.create_oval(50,50,promien,promien,fill="green")


while(True):
    if(keyboard.is_pressed("Up")):
        canvas.delete(kulka)
        promien = promien -10
        kulka = canvas.create_oval(50,50,promien,promien,fill="green")
        time.sleep(0.1)
    if(keyboard.is_pressed("Down")):
        canvas.delete(kulka)
        promien = promien +10
        kulka = canvas.create_oval(50,50,promien,promien,fill="green")
        time.sleep(0.1)



    okienko.update()
