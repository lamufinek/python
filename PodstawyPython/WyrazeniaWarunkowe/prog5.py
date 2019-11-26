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


'''I na koniec dla dociekliwych- albo w sumie to dla wszystkich :P :
Wbrew temu co sobie często myślimy o komputerach, że to jakieś czary,
To jednak procesor (czyli zasadniczy element naszego komputera/systemu komputerowego)
Opiera swoje działanie na dość prostych zjawiskach fizycznych. Potęga procesora wynika z jego złożonośći:
współczesne procesory składają się z wielu milionów elementów elektronicznych (btw. nazywanych tranzystorami)'''

'''Między innymi dzięki działowi matematyki jakim jest LOGIKA, w 20. wieku naukowcy stworzyli
z elementów elektronicznych struktury logiczne- przykładem jest właśnie współczesny procesor. I tu dochodzimy do sedna:
język binarny, czyli zerojedynkowy, czyli zera i jedynki, czyli ciąg np: 010001010100101010010100101010010101,
czyli wyrażenie w systemie dwójkowym (ponieważ opiera się na 2 cyfrach, w opozycji do naszego systemu liczbowego dziesiętnego, bo mamy 10 palców u rąk i nóg)

'''
if("żaba"):
    print("miarka się przebrała!")
