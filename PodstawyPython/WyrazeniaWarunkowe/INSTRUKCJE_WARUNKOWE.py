#Programy przetwarzane (realizowane) są sekwencyjnie- tzm. linijka po linijce
#Program napisany przez programistę w języku python jest tłumaczony na kod binarny (zera i jedynki)
#Ciąg zer i jedynek jest możliwy do przetworzenia przez procesor i może być przechowywany w pamięci RAM (może mieć fizyczną reprezentację w pamięci RAM)
#Ciąg zer i jedynek (tzn. zapis binarny) "jest językiem procesora"
#Python jako język jest językiem programisty i w swojej formie jest zbliżony do języka jakim posługujemy się nacodzień (tj. języka naturalnego)

'''Jeżeli chcemy by poszczególne polecenia/fragmenty kodu były wykonane
zależnie od zaistnienia jakichś warunków (spełnienia jakichś warunków) powinniśmy
wykorzystać wyrażenia warukowe'''

'''Program napisany w języku Python jest "tłumaczony"
(interpretowany tak jak nuty muzyczne) na 'język binarny zrozumiały dla procesora'
przez program zwany INTERPRETEREM '''



if(567>467):            #jeżeli wyrażenie zawarte w nawisie będzie prawdziwe
    print("pryncypał")     #Zostanie zrealizowane polecenie lub polecenia po dwukropku
    
if(467>567):            #jeżeli wyrażenie zawarte w nawisie NIE będzie prawdziwe
    print("dygnitarz")  #Polecenie po dwukropku nie zostanie zrealizowane


###PRZERWA NA HERBATKĘ, SOCZEK, SIKU


#pamiętaj, że w języku Python to wcięcia ze znaków białych (spacji i tabulatorów)
#decydują o tym czy któryś fragment twojego programu jest zawarty w danej strukturze logicznej (if, while, for itp)
#czy jednak nie jest w niej zawarty. I tak poniżej:

if(340>67):
    print("posępny")
    print("dygnitarz")
    print("wąchał")
    print("rzepę") #wszystkie słowa zostaną wyświetlone ponieważ warunek w nawiasie jest spełniony


if(67>340): #czyli wyrażenie w nawisie nie jest prawdziwe, bo czy 67 faktycznie jest większe od 340?!?
    print("narcystyczny")
    print("marynarz")    #słowa poprzedzone Tabulatorem (TAB) nie zostaną wyświetlone ponieważ są cześcią wyrażenia warunkowego 
    print("skonał")     #A warunek w nawisie nie jest spełniony
print("BOOM")           #dopiero słowo BOOM nie jest elementem wyrażenia warunkowego

#Poeksperymentuj

###PRZERWA NA HERBATKĘ, SOCZEK, SIKU



'''I na koniec dla dociekliwych- albo w sumie to dla wszystkich :P :
Wbrew temu co sobie często myślimy o komputerach, że to jakieś czary,
To jednak procesor (czyli zasadniczy element naszego komputera/systemu komputerowego)
Opiera swoje działanie na dość prostych zjawiskach fizycznych. Potęga procesora wynika z jego złożonośći:
współczesne procesory składają się z wielu milionów elementów elektronicznych (btw. nazywanych tranzystorami)'''

'''Między innymi dzięki działowi matematyki jakim jest LOGIKA, w 20. wieku naukowcy stworzyli
z elementów elektronicznych struktury logiczne- przykładem jest właśnie współczesny procesor. I tu dochodzimy do sedna:
język binarny, czyli zerojedynkowy, czyli zera i jedynki, czyli ciąg np: 010001010100101010010100101010010101,
czyli wyrażenie w systemie dwójkowym (ponieważ opiera się na 2 cyfrach,
w opozycji do naszego systemu liczbowego dziesiętnego, bo mamy 10 palców u rąk i nóg)
I tak: skoro nasz procesor to układ elektroniczny, który przetwarza ciąg zer i jedynek:
TUTAJ PAMIĘTAJ- liczby i matematyka są tylko abstrakcją stworzoną przez człowieka by opisać, usystematyzować różne zjawiska!!! 
To "nasze/ludzkie logiczne 0" będzie oznaczało brak napięcia elektrycznego(tego samego napięcia elektrycznego, które kryje się w bateriach :P )
To "nasze/ludzkie logiczne 1" będzie oznaczało obecność napięcia.

Głowa boli, co?
'''
#I dla filozofów: Fizyka+Elektronika+Matematyka+Lingwistyka(nauka o językach)= Współczesny Język Programowania

###PRZERWA NA HERBATKĘ, SOCZEK, SIKU
"""LOGIKA (ten dział matematyki :P ) mówi, że:
NIE Prawda = Fałsz
NIE Fałsz = Prawda
I tak w nawiasie wyrażenia warunkowego możemy zawrzeć nie tylko złożone wyrażenie:
np 45>78, 45+67+89>67, czy 39/3>13*2 ("/" to znak dzielenia, "*" to znak mnożenia)
ale również samo:
0 czyli logiczny fałsz
i każdą inną liczbę, a każda inna liczba to nie 0 czyli nie fałsz, czyli PRAWDA
"""
if(0):  #czyli wewnątrz nawiasu nie fałsz=warunek niespełniony 
    print("grzesznik") #nie zostanie wyświetlony

if(789):    #czyli nie zero, czyli NIE FAŁSZ, czyli PRAWDA
    print("rewolwer")
    print("BOOM")
    print("BOOM")   #rewolwer, bum, bum, bum zostanie wyświetlone
    print("BOOM")
    print("BOOM")


if(789+678):    #a nawet można dodawać: nie zero plus nie zero, to NIE FAŁSZ+NIE FAŁSZ=PRAWDA+PRAWDA=PRAWDA 
    print("maniok") #to taka roślina uprawna, a jej nazwa zostanie wyświetlona


### DOŚĆ na DZIŚ
