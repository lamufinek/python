dzien = int(input("podaj dzień urodzenia (przykład: 04, 18, 31): "))
miesiac = int(input("podaj miesiac urodzenia (przykład: 02, 09, 12): "))
rok = int(input("podaj rok urodzenia (przykład: 1993, 2004): "))


cyfra1 = int(dzien/10)
cyfra2 = dzien%10

cyfra3 = int(miesiac/10)
cyfra4 = miesiac%10

cyfra5 = int((rok/1000))
cyfra6 = int((rok/100)%10)
cyfra7 = int((rok/10)%10)
cyfra8 = rok%10

suma = cyfra1+cyfra2+cyfra3+cyfra4+cyfra5+cyfra6+cyfra7+cyfra8

print(suma)
