print("Hello world!");

x = 2;

y = x + x;

print(y);

napis = "ala ma kota";
napis2 = 'ala ma kota';
#bez różnicy czy jest cudzysłów pojedynczy czy podwóny

nazwisko = "Kowalski";
#długość
len(nazwisko) #8
# indeksowanie ## ważne - zaczyna się indeks od 0 nie od jedynki
nazwisko[0] #K
nazwisko[3] #a
#nazwisko[8] #błąd taki indeks nie istnieje.

liczba = 2;
napis = '2';
#liczba + napis ## takie coś skończy się błędem.

imie = input("Podaj imię");
print("Witaj lamusie o imieniu: ", imie);

zmienna = 5
if (zmienna>2):
    print("zmienna większa od 2")
else:
    print("zmienna mniejsza lub równa 2")


zmienna = 5
if zmienna > 3:
    print("ten kod wykona sie jezeli zmienna jest wieksza od 3")
    print("ten wciaz jest w bloku kodu")
    if zmienna > 4:
        print("zwieksza nawet od 4")
print("ten kod wykona sie zawsze")


lista = [1, 2, 3, 4]
lista2 = ["string1", "string2"]
lista3 = [1, 3, "dupa"]

print(lista[0]) #chcę dostać pierwszy elemet z listy

lista2[0] = "inny string" #nadpisanie elemetu pierwszego w lista 2

lista2.append("string dopisany do listy") #metoda, dzięki której dopisujemy coś do listy

#słowniki
slownik = {
    "klucz": "wartość",
    "klucz2": "wartość",
    "klucz3": "wartość3"
}
print(slownik["klucz2"])

liczba=5
while liczba > 0:
    print("liczba to: ", liczba)
    liczba = liczba-1
print("po pętli")

lista = ["napis1", "napis2", "napis3"]
for element in lista:
    print(element)

for liczba in range(5)
    print(liczba)

def funkcja():
    print("Hello rom function!")

funkcja()

def funkcja2(imie):
    print("Hello ", imie)

funcja2("Tomek")
funcja2("Aga")

def kwadrat(liczba):
    print(liczba* liczba) #funkcja wypisuje wynik na ekran

kwadrat(2)

def kwadrat2(liczba):
    return liczba* liczba #funkcja wynik zapamiętuje wynik w pamięci, można wykorzystać dalej

zmienna = kwadrat2(2)
print(zmienna)
print(kwadrat2(zmienna))

#tworzymy sobie plik txt tekst - z wierszzami doma

with open('tekst') as plik: #domyslnie w trybie r
    for linia in plik:
        print(linia)

with open('tekst') as plik: #domyslnie w trybie r
    linia = plik.readline()
    print(linia)
    linia = plik.readline
    print(linia)

with open('tekst') as plik:
    caly_plik = plik.read()
    print(caly_plik)


