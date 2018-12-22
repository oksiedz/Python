# funkcja główna programu
def main():
    print("Witaj świecie!") # ta funkcja wypisuje napis
    # wiersz poniżej wczytuje dane z klawiatury
    pobrany_napis = input()
    print("Twój napis to: " + pobrany_napis)
# uruchomienie funkcji głównej
if __name__ == "__main__":
    main()

"""
Tutaj następuje obszerne wyjaśnienie funkcji main().
Przyjmowane parametry: żadne
Wartość zwracana: żadna
"""
def main():
    print("Witaj świecie!")
    pobrany_napis = input()
    print("Twój napis to: " + pobrany_napis)
if __name__ == "__main__":
    main()

type() ##funkcja Type służy do zwracania typu zmiennej.

#liczba zespolona
zespolona = -7.4+8.4j
print(type(zespolona))

#konwersja
int(7.0)
float(7)
print(int(5.7))
print(int(-5.7))
str() #konwersja na satring


def main():
    x = 7
    y = 3

    suma = x + y
    print("Dodawanie: " + str(suma))

    roznica = x - y
    print("Różnica: " + str(roznica))

    iloczyn = x * y
    print("Iloczyn: " + str(iloczyn))

    iloraz = x / y
    print("Iloraz: " + str(iloraz))

    reszta = x % y
    print("Reszta z dzielenia: " + str(reszta))


if __name__ == "__main__":
    main()




##### rozwiązanie zadania
def main():
    stop = 0
    while stop == 0:
        print("Podaj w oddzielnych wierszach akceptowanych enterem liczbę, operację matematyczną i następną liczbę");
        zmienna1 = float(input())
        operator = input();
        zmienna2 = float(input())

        if operator == "+":
            wynik = zmienna1 + zmienna2
        elif operator == "-":
            wynik = zmienna1 - zmienna2
        elif operator == "*":
            wynik = zmienna1 * zmienna2
        elif operator == "/":
            wynik = zmienna1 / zmienna2
        elif operator == "%":
            wynik = zmienna1 % zmienna2
        else:
            print("Nieprawidłowy znak operatora")

        print("Twój wynik to:", wynik)

        print("Czy chcesz wykonać kolejne obliczenia? Wpisz literę t lub n.")
        if_continue = input()

        if if_continue == "t":
            stop = 0
            print("Rozpoczynamy kolejne obliczenia.")
        else:
            stop = 1
            print("Konczymy obliczenia.")


if __name__ == "__main__":
    main()