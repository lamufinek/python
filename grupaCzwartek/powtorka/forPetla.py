#prosta pętla drukujaca słowo 10 razy
for i in range(10):
    print("krolik")

###########################################

#pętla uzywajaca zmiennej
zmienna = "jakies slowo"
for i in range(10):
    print(zmienna)

##############################


#petla działajaca "liczba"-razy printujaca zmienną

liczba = 8
zmienna2 = "makaron"

for i in range(liczba):
    print(zmienna2)

####################################


#petla printujaca zmienna wyraz od wartosci 89-189
zmienna3 = 89
zmienna4 = 189
wyraz = "bruuummm"

for i in range(zmienna3,zmienna4):
    print(wyraz)


#petla printujaca liczby od 100 do 200

for x in range(100,200):
    print(x)
    print(x)
    print(x)


#petla printujaca liczby parzyste od 100 do 200
#100,102,104,106
for x in in range(100,200,2):
    print(x)

#petla printujaca liczby parzyste od 200 do 100

for x in in range(100,200,-2):
    print(x)

#petla, ktora 3 razy wywoluje petle, ktora 2 raz printuje słowo

naszeSlowo = "krowa"

for i in range(3):
    for x in range(2):
        print(naszeSlowo)


# ile rzy które słowo zostanie wyprintowane
for i in range(100):
    for j in range(20):
        print("makao")
        for x in range(10):
            print("bambus")
    for h in range(20):
        print("momo")
        for k in range(2):
            for r in range(4):
                print("buku")

#babus 10*20*100=20000
#makao 20*100
#buku 4*2*20*100= 1600
#momo 20*100
