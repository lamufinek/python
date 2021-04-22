
#Rachunek Logiczny
#True jest 1 lub alternatywnie dowolna liczba różna od 0
#False jako 0

# or  +    *

# 1   +    0   =  1
#True or False = True

#1     *     0   =   0
#True and False = False


#    1   +   0    *    0    +   1   =  1+0+1 = 2
if(True or False and False or True):
    print("bobo")
else:
    print("robo")

#   1    +   0   +  1    *    0   +   1   *    0  =  1+0+0+0 = 1
if(True or 7>8 or True and 7>=9 or True and 9>9): #Kacper
    print("robor")

#   1    *   0   +  1    *    0   *   1   *    0  =  0
if(True and 7>8 or True and 7>=9 and True and 9>9): #Miłosz
    print("probor")

#   1    +   0   +  1    +    0   +   1   *    0  =  1
if(True or 7>8 or True or 7>=9 or True and 9>9): #Maks
    print("brobor")


#   1    *   0   +  1    *    0   +   1   *    0  =  0
if(True and 7>8 or True and 7>=9 or True and 9>9): #Bartek
    print("grobor")

#   1    +   0   +  1    *    0   +   1   +    0  =  2
if(True or 7>8 or True and 7>=9 or True or 9>9): #Krzysiek
    print("srobor")

if(jakiś warunek):
    print()
elif(jakis warunek): #ile chcemy elif
    print()
else:

# warunek if, z trzema elif, i z else na końcu, taki że zadziała dopiero else

if(False):
    print(1)
elif(False):
    print(2)
elif(False):
    print(3)
elif(False):
    print(4)
else:
    print(5)



# warunek if, z trzema elif, i z else na końcu, taki że zadziała dopiero 3 elif

if(False):
    print(1)
elif(False):
    print(2)
elif(False):
    print(3)
elif(True):
    print(4)
else:
    print(5)




# napisz warunek badjący czy zmienna a jest mniejsza niż 100 -> a mniejsza niż sto
# a jest większa niż 100 -> a większa niż sto
# a jest równa 100 -> a równa sto

#można zrobić odzielny if dla każdego warunku ale to obciąża komputer
a=2137
if(a>100):
    print("a jest wiksza niz 100")
if(a==100):
    print("a = 100")
if(a<100):
    print("a jest mniejsza niz 100")


# rekomendowane takie rozwiązanie
ad = 2137
if ad > 100:
    print("ad wiksze niż 100")
elif ad == 100:
    print("ad równe 100")
else:
    print("ad mniejsz niż 100")




#Binarne
#2^5    2^4    2^3    2^2    2^1   2^0
#32    16      8      4      2     1
#0     0       0       1     0     0   = dziesiętne 4
#0     1      0       1     1     0   = dziesietne 22
#0     0     1       0     1     1   = dziesietne 11
#1     0     1      1      0     0   = dziesietne 44
#0     1     0      1      1     1   = dziesietne 23
#0     1     1      0      0     1   = dziesietne 25
#0     1     1      0      1     0   = dziesietne 26





#        1 1
#    0 0 0 1 1 0
#+   0 0 1 1 1 0
#________________
#    0 1 0 1 0 0
