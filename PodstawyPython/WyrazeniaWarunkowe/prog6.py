import random

zmienna1=random.randint(1,10)
print(zmienna1)

while(True):
    naszaLiczba=int(input("Wprowadz liczbe od 1 do 10:"))
    if(naszaLiczba==zmienna1):
        print("Zgadles")
    else:
        print("Sprobuj ponownie")
    



