import random
import datetime

NoOfNumbers = int(input('Podaj dlugosc ciagu liczb: '))
randomlist = []
print("Rozpoczecie generowania ciagu liczb.")
for i in range(0, NoOfNumbers):
    randomlist.append(random.random())
print("Zakonczenie generowania ciagu liczb.")

def double_search(startnumber, endnumber):
    print("Podwojne przeszukanie wszystkich elementow")
    max_1 = 0
    max_2 = 0
    starttime = datetime.datetime.now()
    for i in range(startnumber, endnumber):
        if randomlist[i] > max_1:
            max_1 = randomlist[i]
    for i in range(startnumber, endnumber):
        if (randomlist[i] > max_2 and randomlist[i] < max_1):
            max_2 = randomlist[i]
    endtime = datetime.datetime.now()
    print("Maksymalna liczba jest rowna: ", max_1, ", druga co do wielkosci jest rowna: ", max_2, ", czas wyszukiwania wynosi: ", endtime - starttime)
    return endtime - starttime

def single_search(startnumber, endnumber):
    print("Pojedyncze przeszukanie wszystkich elementow")
    max_1 = 0
    max_2 = 0
    starttime = datetime.datetime.now()
    for i in range(startnumber, endnumber):
        if randomlist[i] > max_1:
            max_1 = randomlist[i]
        elif randomlist[i] > max_2:
            max_2 = randomlist[i]
    endtime = datetime.datetime.now()
    print("Maksymalna liczba jest rowna: ", max_1, ", druga co do wielkosci jest rowna: ", max_2, ", czas wyszukiwania wynosi: ", endtime - starttime)
    return endtime - starttime

double_search(0, NoOfNumbers)

single_search(0, NoOfNumbers)



print("Przeszukanie wszystkich elementow metoda turniejowa")


