"""
Na tym etapie należy uświadomić sobie, że jedyne informacje jakie może
przetwarzać komputer (konkretnie procesor)
to ciąg zer i jedynek (np: 100101010101010101010100100101010101010101010101010101010101101010101011001010101101100101011010101010100101011010011010010101011010101001101110111110010101010101010110101010)
Przypomnijmy, że LICZBY I MATEMATYKA to tylko abstrakcyjne pojęcia
stworzone przez człowieka by opisać otaczjący nas świat.
Z punktu widzenia układu elektronicznego jakim jest procesor,
a procesor człowiekiem nie jest i ludzka abstrakcja jest mu obca,
nasza "ludzka liczba 1" będzie oznaczała obecność napięcia elektrycznego
w danej sekcji logicznej
nasza "ludzka liczba 0" będzie oznaczała NIEobecność napięcia elektrycznego
w danej sekcji logicznej
Skoro wszystkie dane jakie przetwarza komputer są przechowywane za pomocą
zer i jedynek to spróbujmy zapisać jakąś liczbę binarnie (tj. dwójkowo):
"""
print(0b1001001) #kiedy chcemy zapisać liczbę binarnie musimy poinformować
                #o tym INTERPRETER, dlatego zaczynamy zapis takiej liczby od "0b"
                #"0b" oznacza dla Interetera: "Hej Interpreter, traktuj tę liczbę jako zapisaną binarnie"
                #by Interpreter nie pomyślał,
                #że 1001001 oznacza :jeden milion i tysiąc jeden" w znaczeniu dzisiętnym 
                #powyższe będzie skutkowało wyświetleniem liczby 73
                #(oczywiście, w naszym ludzkim systemie dziesiętnym)

#System binarny jest systemem pozycyjnym, tak jak nasz system dziesiętny
#Im wyższa pozycja cyfry (a mamy tylko 0 i 1 w systemie dwójkowym) tym większe jej znaczenie
#tym większą wagę ma taka cyfra
# no to lecimy:

print(0b000000) #wyświetli 0
print(0b000001) #wyświetli 1
print(0b000010) #wyświetli 2
print(0b000011) #wyświetli 3

"""
WOW co tu się stało?!?!?! Czy z powyższych przykładów wynika, że
system dwójkowy jest banalny i jeśli dodamy binarne 1 do binarnego 2 to
otrzymam binarne 3?!!!???! I wszystko to sprowadza się do banalnego dodawania
w słupku?!!!???!! NIEMOŻLIWE !!!!!

Czy nasz, ludzki system dziesiętny (gdybyśmy mieli siedemnaście palcy,
to nasz system liczbowy pewno byłby siedemnastkowy) nie opiera się na tych
samych banalnych zasadach?!
Czy przypadkiem nie jest tak, że:

    2100
 +    53
 =  2153
"""
###PRZERWA NA HERBATKĘ, SOCZEK, SIKU i REFLEKSJĘ

#No to dalej:

print(0b000100) #wyświetli 4

# żeby było 5??:
#     0b000100 to 4
#     0b000001 to 1
print(0b000101) #daje nam 5! To nie może być takie proste!

#Jak myślicie, jak będzie z 6?
#                        0b000101   czyli 5
#Wystarczy, że tę jedynkę       ^   przesuniemy o jedno miejsce w lewo
#I mamy:                 0b000110   czyli 6, ponieważ system dwójkowy jest systemem pozycyjnym 
print(0b000110)


"""
    0b000101
+   0b000001
=   0b000110 (bo przesuwamy na kolejną pozycję
                tak jak w dodawaniu w systemie dziesiętnym)
"""


print(0b000111) # da 7, bo 0b000110 to 6
                # +        0b000001 to 1


#No a 8?
print(0b001000) #daje 8
print(0b010000) #daje 16
print(0b100000) #daje 32

"""
O co tutaj chodzi?!? Ano o to, że kolejne potęgi liczby 2
tworzą kolejne pozycje. Sprawdźmy dla liczby binarnej, która ma 16 pozycji:
0000000000000000===>0
0000000000000001===>1
0000000000000010===>2      =2 do potęgi 1
0000000000000100===>4      =2 do potęgi 2
0000000000001000===>8      =2 do potęgi 3
0000000000010000===>16     =2 do potęgi 4
0000000000100000===>32     =2 do potęgi 5
0000000001000000===>64     =2 do potęgi 6
0000000010000000===>128    =2 do potęgi 7
0000000100000000===>256    =2 do potęgi 8
0000001000000000===>512    =2 do potęgi 9
0000010000000000===>1024   =2 do potęgi 10
0000100000000000===>2048   =2 do potęgi 11
0001000000000000===>4096   =2 do potęgi 12
0010000000000000===>8192   =2 do potęgi 13
0100000000000000===>16384  =2 do potęgi 14
1000000000000000===>32772  =2 do potęgi 15

                        
No to jaką maksymalną liczbę dziesiętną można zapisać za pomocą liczby
binarnej o 16 pozycjach? Wystarczy dodać:

 0000000000000000
+0000000000000001
+0000000000000010      
+0000000000000100      
+0000000000001000  
+0000000000010000    
+0000000000100000
+0000000001000000
+0000000010000000
+0000000100000000
+0000001000000000
+0000010000000000
+0000100000000000
+0001000000000000
+0010000000000000
+0100000000000000
+1000000000000000
=1111111111111111


                 0
+                1
+                2      
+                4      
+                8      
+               16     
+               32     
+               64     
+              128    
+              256    
+              512    
+             1024   
+             2048   
+             4096   
+             8192   
+            16384  
+            32768
=            65535

No to sprawdźmy:
"""
#w wielu językach programowania znak "==" służy do zadania pytania czy jakieś
#dwie liczby lub wartości są sobie równe

if(0b1111111111111111 == 65535):  
    print("###PRZERWA NA HERBATKĘ, SOCZEK, SIKU i REFLEKSJĘ")

#okazuje się, że binarne 0b1111111111111111 to ta sama wartość
#co nasz, dzisiętne 65535 czyli:

###PRZERWA NA HERBATKĘ, SOCZEK, SIKU i REFLEKSJĘ
    

#No to juz wiemy, że procesor to układ elektroniczny, który
#ma jakąś swoją logiczną strukturę, logiczną organizację, i że procesor
#przetwarza wyłącznie informacje zakodowane jako 0 i 1(liczby,tekst,grafikę,obrazy,dźwięk)
#Słowo Komputer wzięło się od angielskiego słowa "compute" czyli "obliczać"
#i jak nazwa sugeruje główne zadanie komputera to obliczanie
#a co zabawne wszystkie skomplikowane operacje mogą być wykonane przez komputer
#za pomocą dodawania- dodawanie dwóch wartości jest elementarną operacją realizowaną prze komputer
#KAŻDA OPERACJA MATEMATYCZNA MOŻE ZOSTAĆ ZREALIZOWANA ZA POMOCĄ DODAWANIA
#Stwierdzenie to może niektórym wydać się nieco szalone, ale wiele wyjaśni
#się w dalszej części kursu, a jeszcze więcej na wyższych szczeblach edukacji :P
#Na razie przyjrzyjmny się w jaki sposób komputer wykonuje elementarną operację dodawania:

print(0b0000001+0b0000010) #zwróci nam liczbę 3


    

