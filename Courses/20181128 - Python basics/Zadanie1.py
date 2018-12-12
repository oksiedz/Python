slownik ={}

with open('oceny.txt') as oceny:
    for linia in oceny:
        linia = linia.strip() #ta funkcja usuwa wszelkie znaki, które nie są znakami - czyli bałe sacje (usuwa białe znaki z początku  ikońca linii)
        podzielone = linia.split() #przyjmuje argument po ktorym ma podzielic -- domyslny argument spacje
        nazwisko = podzielone[0]
        ocena = podzielone[1]
        ocena = int(ocena) #konwersja na int jeżeli string wyglada jak liczba
        slownik[nazwisko] = ocena

najwyzsza_ocena = 0
najwyzsza_ocena_nazwisko = None
najniznsza_ocena = 10000
najniznsza_ocena_nazwisko = None
suma = 0

for nazwisko in slownik:
    ocena = slownik[nazwisko]
    if ocena > najwyzsza_ocena:
        najwyzsza_ocena = ocena
        najwyzsza_ocena_nazwisko = nazwisko
    if ocena < najniznsza_ocena:
        najniznsza_ocena = ocena
        najniznsza_ocena_nazwisko = nazwisko
    suma += ocena #to jest dokadnie to samo co : suma = suma + ocena

print("najwyzsa ocena to: ", najwyzsza_ocena," uzyskana przez ", najwyzsza_ocena_nazwisko)
print("najwyzsa ocena to: ", najniznsza_ocena," uzyskana przez ", najniznsza_ocena_nazwisko)
print("Średnia: ", suma/len(slownik)) #len zwroci dlogosc na naszym slowniku czyli dlugosc