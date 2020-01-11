from tkinter import *


tresc = "" 
  
  

def press(znak): 
     
    global tresc 
  
    
    tresc = tresc + str(znak) 
  
    
    wyswietlacz.set(tresc) 
  
  

def rownaSie(): 
    
   
    global tresc 
  
        
    wynik = str(eval(tresc)) 
  
    wyswietlacz.set(wynik) 
  
         
    
  
     

okienko = Tk()
okienko.title("Nasz Kalkulator")
okienko.geometry("260x500")

wyswietlacz = StringVar() 
  
    
okienkoWyswietlacza = Entry(okienko, textvariable=wyswietlacz,width=11) 
  
    
okienkoWyswietlacza.grid(row= 0,column=0) 
  
wyswietlacz.set('Wpisz równanie') 


przycisk1 = Button(okienko, text=' 1 ', fg='grey', bg='white', 
                     command=lambda: press(1), height=1, width=11) 
przycisk1.grid(row=2, column=0) 

przycisk2 = Button(okienko, text=' 2 ', fg='grey', bg='pink', 
                     command=lambda: press(2), height=1, width=11) 
przycisk2.grid(row=2, column=1)

przycisk3 = Button(okienko, text=' 3 ', fg='grey', bg='light blue', 
                     command=lambda: press(3), height=1, width=11) 
przycisk3.grid(row=2, column=2)

przycisk4 = Button(okienko, text=' 4 ', fg='grey', bg='light blue', 
                     command=lambda: press(4), height=1, width=11) 
przycisk4.grid(row=3, column=0) 

przycisk5 = Button(okienko, text=' 5 ', fg='grey', bg='pink', 
                     command=lambda: press(5), height=1, width=11) 
przycisk5.grid(row=3, column=1)

przycisk6 = Button(okienko, text=' 6 ', fg='grey', bg='pink', 
                     command=lambda: press(6), height=1, width=11) 
przycisk6.grid(row=3, column=2)

przycisk7 = Button(okienko, text=' 7 ', fg='grey', bg='pink', 
                     command=lambda: press(7), height=1, width=11) 
przycisk7.grid(row=4, column=0) 

przycisk8 = Button(okienko, text=' 8 ', fg='grey', bg='light blue', 
                     command=lambda: press(8), height=1, width=11) 
przycisk8.grid(row=4, column=1)

przycisk9 = Button(okienko, text=' 9 ', fg='grey', bg='light blue', 
                     command=lambda: press(9), height=1, width=11) 
przycisk9.grid(row=4, column=2)

plus = Button(okienko, text=' + ', fg='grey', bg='light blue', 
                     command=lambda: press("+"), height=1, width=11)
plus.grid(row=5, column=0)

przycisk0 = Button(okienko, text=' 0 ', fg='grey', bg='light blue', 
                     command=lambda: press(0), height=1, width=11)
przycisk0.grid(row=5, column=1)

minus = Button(okienko, text=' - ', fg='grey', bg='light blue', 
                     command=lambda: press("-"), height=1, width=11)
minus.grid(row=5, column=2)

mnozenie = Button(okienko, text=' * ', fg='grey', bg='light blue', 
                     command=lambda: press("*"), height=1, width=11)
mnozenie.grid(row=6, column=0)

przyciskRowna = Button(okienko, text=' = ', fg='grey', bg='light blue', 
                     command=lambda: rownaSie(), height=1, width=11)
przyciskRowna.grid(row=6, column=1)

dzielenie = Button(okienko, text=' / ', fg='grey', bg='light blue', 
                     command=lambda: press("/"), height=1, width=11)
dzielenie.grid(row=6, column=2)












okienko.mainloop()

