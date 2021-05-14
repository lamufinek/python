from random import *

#


def maks(tablica):
    najwieksza=tablica[0]
    for liczba in tablica:
        if(liczba>najwieksza):
            najwieksza=liczba
    return najwieksza


#funkcja "losowaTablica", która zwraca tablicę liczb, gdzie elementów w tablicy jest A, i elementy są losowane z przedziału B do C
#randint(B,C)

def losowaTablica(ile,od,do):
    tablica=[]
    for i in range(ile):
        tablica.append(randint(od,do))
    return tablica




TablicaA = losowaTablica(1000,50,150) #tysiąc elementów z przedziału 50 do 150
print(maks(TablicaA))
