from random import *

B = []

for i in range(100):
    B.append(randint(1,1000))

C = []

for i in range(1000):
    C.append(randint(1,1000))

A = [89,56,107,67,89,45,78,89,67,56,78,90,43,32,21,7,8,97,4,5,6,78,56,89,67,999,33,12,123,45,66,1788,123,345,567,78,656,456,788,789,785]



def najwiekszaWartosc(Tablica):
    najwieksza = Tablica[0]
    for liczba in Tablica:
        if liczba>najwieksza:
            najwieksza = liczba
    print(najwieksza)

najwiekszaWartosc(A)
#najwieksza = A[0]
#for liczba in A:
#   if liczba>najwieksza:
#       najwieksza = liczba
#print(najwieksza)


najwiekszaWartosc(B)
najwiekszaWartosc(C)
