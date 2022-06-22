def xdd(a,b):
    suma = a+b
    return suma

wynik =xdd(xdd(9,4),xdd(xdd(9,4),xdd(9,4)))
print(wynik + 5)




tekst1 = "I tak, powołanie właściwej Organizacji, po uprzednim opracowaniu optymalnego modelu biznesowego dla takowej, jak i wprowadzenie rozwiązań w ramach Platformy, stanowią odrębne koncepcje, z których każda mogłaby być rozwijane niezależnie. Co istotne, zarówno powołanie Organizacji, której celem jest redukcji niedostatków w obszarze zarządzania i architektury badań wdrożeniowych, przy jednoczesnym odstąpieniu od działań zmierzających do uruchomienia Platformy, jak i samo podjęcie prac architektonicznych i wdrożeniowych związanych z Platformą, przy jednoczesnym odstąpieniu od powoływania właściwej Organizacji, może doprowadzić do zaistnienia pozytywnych zmian na rynku obsługi badań wdrożeniowych. Jednak to właśnie ewentualna integracja obu rozwiązań zdaje się być obdarzona potencjałem doprowadzenia do wystąpienia efektu synergii i wytworzenia znacznych korzyści w obszarze stymulacji i wspierania procesów badawczo-rozwojowych.  "

tekst2 = ["w","s","o","k","o"," ","n","a"," ","g","o","r","z","e"," ","r","o","s","l"]



for znak in tekst1:
    print(znak)



def licznikA(tekst):
    liczbaA = 0
    for litera in tekst:
        if(litera == "a"):
            liczbaA = liczbaA + 1
    return liczbaA


print("liczba wystapien litery a w podanym tekscie wynosi: " + str(licznikA(tekst1)))

