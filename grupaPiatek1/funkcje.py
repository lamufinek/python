
# prezentacja funkcji

def naszaFunkcja(a,b,c,d):
    najwieksza = a
    if(najwieksza<b):
        najwieksza = b

    if(najwieksza<c):
        najwieksza = c

    if(najwieksza<d):
        najwieksza = d

    print(najwieksza)


naszaFunkcja(10,1000,15,153)

naszaFunkcja(20000000,1,-20000000,53000)

naszaFunkcja(185784750,10034534530,13453453455,13453453454353)



naszaFunkcja(1345345340,-1034534500,1345345345345,134534534534553)




# zdefinuj funckję "guru" z dwoma argumentami ("a" i "b"), która to funkcja printuje sumę "a" i "b"
#wykonaj wywołanie funkcji
def guru(a,b):
    print(a+b)

guru(3,9)
guru(3,5)
guru(3,7)




def guruPetla(a,b,c):
    for i in range(c):
        print(a+b)

guru(3,9)
guru(3,5)
guru(3,7)


guruPetla(5,9,10)
guruPetla(2,1,5)



#definuj funkcje "buru" bez argumentów, która sto razy printuje "boom"


def buru():
    for i in range(100):
        print("boom")


# zdefiniuj funkcje, która sprawdza czy podana liczba jest parzysta- jeśli parzysta to print "parzyszt", jesli nie, print "nieparysta"
#  a%b     <-- reszta z dzielenia a przez b     if(liczba%2==0):
