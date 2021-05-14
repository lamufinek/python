from random import *

# zdefinujcie funkcję, która zwraca największy element z tablicy

Tablica = [238127381273,12938198312,29183737129,12398103981230,1092830129830921,01239810983121809]



def najwiekszyElement(tablica):
    najwieksza=tablica[0]
    for liczba in tablica:
        if(liczba>najwieksza):
            najwieksza=liczba
    return najwieksza


najwiekszyElement(Tablica)

#napisze funkcje "losowaTablica", która zwraca tablicę liczb, długości A, gdzie liczby losowane są z zakresu B do C




tabliczunia = losowaTablica(100,34,89)
