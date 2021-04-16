#petla a-razy drukuje słowo "but"
a= 13
for i in range(a):
    print("but")


#petla drukujaca wszystkie liczby od 300    do 1000:

for i in range(300,1000):
    print(i)


#petla drukujaca parzyste liczby od 300    do 1000:

for i in range(300,1000,2):
    print(i)



#petla drukujaca nieparzyste liczby od 300    do 1000:
#V1:
for i in range(300,1000):
    if(i%2!=0):
        print(i)


#V2:
for i in range(300,1000):
    if(i%2==1):
        print(i)

#V3:
for i in range(301,1000,2):
    print(i)


# a równa się b:  a==b
# a > b
#a < b
# a >= b : a większe lub równe b
# a <= b : a mniejsze lub równe b
# a != b : a różne od b
#not(a==b) : a nie równa się b

# pętla for która printuje wszystkie wartości od 1000 do 300
for i in range(1000,300,-1):
    print(i)



for i in range(100):
    for j in range(10):
        print("mongo") #mongo 10*100
        for o in range(8):
            print("bongo") # 8*10*100 = 8000
        for r in range(90):
            for d in range(3):
                print("diki") # 3*90*10*100=270000
            for x in range(4):
                print("zibi") # 4*90*10*100
        for h in range(2):
            print("twiti") #2*10*100
