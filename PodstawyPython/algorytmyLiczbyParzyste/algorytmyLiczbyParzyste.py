import keyboard
def funkcjaMnozenia():                      #tworzymy prostą funcję, która mam za zadanie zwrócić wynik
    liczba = int(input("Wpisz liczbe:"))    #mnożeniea dwóch liczb
    while(True):                               #chcemy by użytkownik wprowadził parzystą liczbę
        if(funkcjaParzystosci(liczba)):         #jeśli wprowadza nieparzystą, to pytamy jeszcze raz
            break
        liczba = int(input("Wpisz liczbe:"))

    licznik = int(input("Wpisz mnożnik:"))   #patrzysty mnożnik jak wyżej
    while(True):
        if(funkcjaParzystosci(licznik)):
            break
        licznik = int(input("Wpisz mnożnik:"))

    wynik=0

    while(True):
        wynik = wynik+liczba                #wynik jest zwiększany co krok pętli, aż do momentu
        licznik = licznik - 1
        if(licznik <= 0):                   #kiedy licznik nie spadnie do zera
            break

    print(wynik)

def funkcjaParzystosci(liczba):             #funcka sprawdza parzystość liczby (za pomocą operatora %, czyli reszta z dzielenia)
    if(liczba%2==0):                        #resszta z dzielenia liczby parzystej przez 2 równa się 0
        return(True)                        # dla liczb parzystych zwraca True
    else:
        return(False)

while(True):
    funkcjaMnozenia()                       #wywołujemy funkcję w każdym przebiegu pętli
    if(keyboard.is_pressed("q")):           #po wciśniećiui q wychozimy z pętli programu
        break
