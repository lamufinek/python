
# pętla for, która 10 razy printuje słowo

for i in range(10):
    print("słowo")

############################################
# petla for drukujaca słowo a-razy
a = 523
for i in range(a):
    print("słowo")

############################################
# petla for drukujaca wszystkie liczby od 0 do a
a=100
for i in range(0,a):
    print(i)
##############################################
#petla drukujaca wszystkie liczby od a do b
a=100
b=200

for i in range(a,b):
    print(i)


#petla drukujaca wszystkie parzyste wartości od 100 do 200:
a=100
b=200

for i in range(a,b,2):
    print(i)

#####################


#petla drukujaca wszystkie parzyste wartości od 200 do 100:


a=100
b=200

for i in range(b,a,-2):
    print(i)



##############################################



for i in range(100,200):
    print("mango") #wykonane 100 razy
    for gogo in range(10):
        print("tango") #wykonane 100*10=1000
        print(i)
    for togo in range(20):
        print("masło") #wykonany 20*100=2000
        for rogo in range(5):
            print("zibi") #wykonane 5*20*100= 10000
