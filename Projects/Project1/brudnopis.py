import random
import datetime
import math

NoOfNumbers = 9
#NoOfNumbers = int(input('Podaj dlugosc ciagu liczb: '))
randomlist = []
print("Rozpoczecie generowania ciagu liczb.")
for i in range(0, NoOfNumbers):
    randomlist.append(random.random())
    print(randomlist[i])
print("Zakonczenie generowania ciagu liczb.")

#ogarnąć to w pętli while z brake gdy liczba winnerów będzie równa 1 - to jest max

#podział na pary
listofpairs = []
n = int(math.ceil(NoOfNumbers / 2))
print ("liczba par", n)
for i in range(0, n):
    if 2*i+1<NoOfNumbers:
        listofpairs.append(str(randomlist[2*i]) + ";" + str(randomlist[2*i+1]))
    else:
        listofpairs.append(str(randomlist[2*i])+";")
for i in range(0,n):
    print(listofpairs[i])

#porównanie par
listofwinners = []
listofloserpairs = []
for i in range(0,n):
    pairforcomparison = listofpairs[i].split(";")
    if pairforcomparison[1] =="":
        listofwinners.append(pairforcomparison[0]+";")
    elif pairforcomparison[0]>pairforcomparison[1]:
        listofwinners.append(pairforcomparison[0])
        listofloserpairs.append(str(pairforcomparison[0])+";"+str(pairforcomparison[1]))
    else:
        listofwinners.append(pairforcomparison[1])
        listofloserpairs.append(str(pairforcomparison[1])+";"+str(pairforcomparison[0]))


listofpairs = listofwinners
listofwinners = []
print(len(listofpairs))



print("Lista wygranych")
for i in range(0,len(listofpairs)):
    print(listofpairs[i])
