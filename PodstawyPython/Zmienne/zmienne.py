"""
W poprzedniej sekcji "liczby binarne" dyskutowaliśmy na temat sposóbu
w jaki komputer przechowuje zakodowane informacje. Wskazaliśmy, że zasadniczo
każda informacja przechowywana w pamięci komputera zakodowana jest przy użyciu
ciągu zer i jedynek. I tak: za pomocą zer i jedynek zakodowana będzie liczba z
systemu dziesiętnego (tj. systemu liczbowego, którym my operujemy na codzień),
litera (zainteresowanych zapraszam do wyszukania hasła "tabela ASCII" w wyszukiwarce)
, cały tekst, nagranie dźwiękowe, obraz, zdjęcie, grafika, czy film
(film jest kombinacją dużej ilości zdjęć/obrazów i nagrania dźwiękowego).

KAŻDA INFORMACJA, KTÓRĄ KOMPUTER PRZETWARZA JEST ZBIOREM ZER I JEDYNEK.

Taka sytuacja wynika po pierwsze ze sposobu w jaki skonstruowany jest procesor:
jest złożony z elementów elektronicznych (zwanych tranzystorami), które tworzą
bardzo rozbudowane struktury logiczne- w znacznym uproszczeniu, procesor jest jedną
wielką strukturą logiczną- a same informacje, które procesor przetwarza to
zera i jedynki symbolizujące brak napięcia elektrycznego (zero) i obecność napięcia (jeden)
Przypominam, że chodzi o to samo napięcie, które powoduje przepływ prądu w latarce,
kiedy umieścimy w niej baterie :P

Po drugie wszystkie informacje przetwarzane przez komputer zapisane są jako zera i jedynki
ponieważ w wypadku zer i jedynek mamy możliwość łatwego zapisu danych w pamięci
komputera.

Uważam, że na tym etapie edukacji dobrze byłoby wyobrażać sobie pamięć komputera
jako gigantyczne pole uprawne, na którym zamiast ziarenek mamy włożone maleńkie magnesy.
Magnes posiada 2 bieguny: "+" i "-". Bigun dodatni jednego magnesu będzie przyciągał
biegun ujemny drugiego magnesu. Na razie wszystkie magnesy na naszym polu są zwrócone
ku nam swoimi biegunami dodatnimi. Załóżmy, że biegun dodatni oznacza 0.

+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +

jeśli zechcemy zapisać do pamięci liczbę 25 (czyli binarnie 00000000011001),
wystarczy w jakimś wierszu zapisać poprzykładać biegun ujemny jakiegoś
"magnesu zapisującego". Taki magnes przyłożyłem na miejscu 1. 4. oraz 5. od prawej
w wierszu pierwszym. Teraz odpowiednie magnesy są zwrócone do nas biegunami ujemnymi
, a my w pamięci mamy zapisaną liczbę 25 (czyli binarnie 00000000011001):

+ + + + + + + + + + + + + - - + + -
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + +

W rzeczywistości każdy wiersz w pamięci komputera posiada swój adres



"""
