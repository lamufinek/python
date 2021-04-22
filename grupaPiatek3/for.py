
# pętla for, która wyświetla -a razy słowo "mangusta"
a = 13

for i in range(a):
    print("mangusta")

#petle for która wypisuje wszystkie liczby od 0 do 100

for x in range(0,100):
    print(x)


#petla wypisujca liczby od 100 do 125

for c in range(100,125):
    print(c)

#petla wypisujaca parzyste liczby od 100 do 200

for i in range(100,200,2):
    print(i)

#petla wypisujaca nieparzyste liczby od 100 do 200
#V1:
for i in range(101,200,2):
    print(i)

#V2:
# a%b to reszta z dzielenia a przez b
for i in range(100,200):
    if(not(i%2==0)):
        print(i)

#V3:
for i in range(100,200):
    if((i%2==1)):
        print(i)

Która pętla zrobi robote:
A)v1





# czy a jest równe b:                  if(a==b):
# od teraz a jest równy b :             a=b
# od teraz a jest równy 5 :             a=5
# czy a jest większe od b :             if(a>b):
# czy a jest mniejszy od b :            if(a<b):
# czy a jest większe lub równy b :      if(a>=b):
# czy a jest mniejszy lub równy b :      if(a<=b):
# czy a jest nierówny b :               if(not(a==b)):   lub if(a!=b)  lub    if(a==not(b))

#V3:
for i in range(100,200):
    if((i%2!=0)):
        print(i)



# pętla printujaca wszystkie licby od 1000 do 300

#wersja niekonwencjonalna Kuby
for i in range(-1000,-300):
    print(i*(-1))

#wersja konwencjonane:
for i in range(1000,300,-1):
    print(i)



######################################################

for i in range(100):
    for j in range(10):
        print("mongo")
        for o in range(8):
            print("bongo")
        for r in range(90):
            for d in range(3):
                print("diki")
            for x in range(4):
                print("zibi")
        for h in range(2):
            print("twiti") 
