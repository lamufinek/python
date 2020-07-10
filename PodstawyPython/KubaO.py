#Dzisiejsze zajecia: petla for
#Program zapisany w języku python składa się z instrukcji
#Instrukcje wykonywane (a ściślej interpretowane są przez interpreter)
#linijka po linijce- mówimy sekwencyjnie
#jeśli w kolejnych trzech linijka zapisane są instrukcje:

zmienna1 = 10
zmienna2 = 50
zmienna3 = zmienna1 - zmienna2

# to w kolejnych krokach procesor zapisze w pamięci wartości 10 i 50
# a następnie doda je do siebie, a wynik tego dodawania również zostanie zapisany
#Wiele języków programowania, w tym również Python, dostarczam ciekawgo
#mechanizmu jakim jest pętla- jedną z częściej używanych pętli jest pętla "for"

for element in range(0,50):
    print(zmienna3)

#powyższa pętla wyświetli 50 razy wartość zapisaną w pamięci jako zmienna3 (aktualnie zmienna3=-40)
#Składnia pętli for jest następująca (for to z angielskiego "dla")
#po słowie for programista definiuje nazwę zmiennej, która jest wewnętrzną zmienną w pętli
#To oznacza, że poza pętlą ta zmienna nie obwowiązuje (nazwa zmiennej nie jest rozpoznawan prze #interpreter języka python). Tutaj nazwana jest "element" (może być dowolna)
#"in range" to słowa kluczowe języka Python i oznaczają "w zbiorze/w zakresie"- tutaj zbiór ma 50 #elementów ponieważ rozważamy wyłącznie liczby całkowite
#nasza pętla wykona jakąś zadaną operację dla każdego elementu z podanego zbioru (0,50)
#50 razy wyświetlona zostanie wartość zmienna3
#dzięki pętli nie ma konieczności wielokrotnego zapisywania tych samych sekwencji instrukcji
#prawdziwy potencjał pętli for ma jednak związek z wymienioną zmienną wewnętrzną pętli

for i in range(0,1000):
    print(i*2)
    
#W każdymn kolejnym przebiegu pętli zmienia się wartość zmiennej i (1,2,3,4,5... 1000)
#Dzięki temu pętla wyśwoetli liczby parzyste od 0,2000, gdzie * to znak mnożenia

from turtle import * #w naszym programie użyjemy biblioteki turtle

#za pomocą biblioteki turtle wykreślimy ciekawy wzór, gdzie długość każdej kolejnej
#prostej zależna będzie od zmiennej wewnętrznej pętli

for odcinek in range(0,1000):    #wartosc zmniennej bedzie coraz wieksza w kolejnych przebiegach petli: odcinek= 1,2,3,4,5,6,....1000
    forward(odcinek)			#do przodu o wartość zmiennej odcinek
    left(243)				#i skręcamy o zadany kąt 243, warto spróbować różnych kątów
    
    
#Możemy również rozbudować strukturę pętli o wewnętrzne instrukcje warunkowe (if= angielskie "jeżeli")
#"jeżeli jakiś warunek jest spełniony, czyli prawdziwy, czyli po angielsku truth, czyli jest prawdą, czyli True"
# if(6+4>5) = if(True):
#	instrukcja, ktora zostanie wykonana bo warunek jest spełniony	
# if(9-14>0) = if(False):
#	instrukcja, ktora nie zostanie wykonana bo warunek nie jest spełniony
#W każdym kolejnym przebiegu pętli będziemy sprawdzali wartość zmiennej odcinek
# i w zależności od wartości tej zmiennej będziemy ustawiali inny kolor kursora

for odcinek in range(0,1000):
    if(odcinek>0 and odcinek<200):		#weryfikujemy czy odcinek miesci się w zakresie od
	color("deep pink")			#0 do 200 jeśli tak, to ustawiamy kolor "deep pink"
    elif(odcinek>200 and odcinek<400):		#jeśli dlugosc odcinka nie miescila sie w zbiorze liczb 0 do 200,
	color("light blue")			#to szukamy miedzy 200 a 400 i ustawiamy kolor "light blue" jeśli znajdziemy
    elif(odcinek>400 and odcinek<600):		#"elif" to skrót od angielkiego else if = "w przeciwnym razie jeśli"
	color("orange")				#czyli jeśli żaden warunek powyżej nie był spełniony to może ten jest
    elif(odcinek>600 and odcinek<800):		#w momencie kiedy interpreter trafi na warunek spełniony (prawdiwy/True),
	color("purple")				#wykonuje zadaną instrukcję i nie sprawdza kolejnych warunków "elif"-zmnienia kolor 
    elif(odcinek>800 and odcinek<1000):
	color("gold")
    forward(odcinek)				#instrukcje takie same jak w poprzedmi przykładzie
    left(243)					#do przodu o odcinek i w lewo o 243 stopnie	

    



    
