import keyboard
import time
from tkinter import *


okienko = Tk()
rysunek = Canvas(okienko, width = 300, height = 300)
rysunek.pack()
kulka = rysunek.create_oval(150,150,160,160,fill="red")
kierunek=6
pozycja=150

while(True):
    time.sleep(0.1)
    rysunek.move(kulka,0,kierunek)
    pozycja=pozycja+kierunek
    rysunek.update()
    if(pozycja>300 or pozycja<0 ):
        kierunek=-1*(kierunek)
    

