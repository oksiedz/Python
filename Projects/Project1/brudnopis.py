import random
import datetime
import math

NoOfNumbers = 10
#NoOfNumbers = int(input('Podaj dlugosc ciagu liczb: '))
randomlist = []
print("Rozpoczecie generowania ciagu liczb.")
for i in range(0, NoOfNumbers):
    randomlist.append(random.random())
    print(randomlist[i])
print("Zakonczenie generowania ciagu liczb.")

#ogarnąć to w pętli while z brake gdy liczba winnerów będzie równa 1 - to jest max

listofpairs = []
listofloserpairs = []
listofnumbers = randomlist
koniec_szukania = 0
listofwinners = []
change_the_listofnumbers = 0
while (koniec_szukania == 0):
    
    if change_the_listofnumbers == 1:
        listofnumbers = listofwinners
        listofwinners = []
    #podział na pary
    n = int(math.ceil(len(listofnumbers) / 2))
    print ("liczba par", n)
    
    if n == 1:
        koniec_szukania = 1
        if float(listofnumbers[0]) > float(listofnumbers[1]):
            max_1 = listofnumbers[0]
            listofloserpairs.append(str(listofnumbers[0])+";"+str(listofnumbers[1]))
        else:
            max_1 = listofnumbers[1]
            listofloserpairs.append(str(listofnumbers[1])+";"+str(listofnumbers[0]))
    else:
        for i in range(0, n):
            if 2*i+1<len(listofnumbers):
                #listofpairs.append(str(listofnumbers[2*i]) + ";" + str(listofnumbers[2*i+1]))
                if listofnumbers[2*i] > listofnumbers[2*i+1]:
                    listofwinners.append(listofnumbers[2*i])
                    listofloserpairs.append(str(listofnumbers[2*i])+";"+str(listofnumbers[2*i+1]))
                else:
                    listofwinners.append(listofnumbers[2*i+1])
                    listofloserpairs.append(str(listofnumbers[2*i+1])+";"+str(listofnumbers[2*i]))
            else:
                #listofpairs.append(str(listofnumbers[2*i])+";")
                listofwinners.append(str(listofnumbers[2*i]))
    print("Lista par które przegrały w pętli")
    for i in range(0, len(listofloserpairs)):
        print(listofloserpairs[i])

    print("lista wygranych w pętli")
    for i in range(0, len(listofwinners)):
        print(listofwinners[i])


    change_the_listofnumbers = 1

print("Lista par które przegrały")
for i in range(0, len(listofloserpairs)):
    print(listofloserpairs[i])

print("lista wygranych")
for i in range(0, len(listofwinners)):
    print(listofwinners[i])


print("Maksymalna liczba to:", max_1)
 