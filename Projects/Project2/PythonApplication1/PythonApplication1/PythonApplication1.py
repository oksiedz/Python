
import random
import datetime
##import math

#NoOfGeneratedNumber - number of items in array to be sorted
noOfGeneratedNumber = 2000

#array with random numbers
listToBeSorted = []
#array with list of results of sorting
listOfResults = []
#array with sorted array ASC
listSortedAsc = []
#array with sorted array DESC
listSortedDesc = []

#inputType - R - random, A - sorted ascending, D - sorted descending


print("Rozpoczęcie generowania ciagu liczb losowych")
for i in range(0, noOfGeneratedNumber):
    listToBeSorted.append(float(random.random()))
print("Zakończenie generowania ciagu liczb losowych")

print("Nieposortowany ciąg:")
#notsorted
for i in range(len(listToBeSorted)):
	print(listToBeSorted[i])

#Selection sort
def selectionSort(inputArray, inputType):
	#Array to be sorted
	print("Selection sort start")
	A = inputArray
	startTime = datetime.datetime.now()
	for i in range(len(A)): 
		#Find the min value in the remaining not sorted part of array
		min_idx = i 
		for j in range(i+1, len(A)): 
			if A[min_idx] > A[j]: 
				min_idx = j 
		#Swap the minimum with the first array element
		A[i], A[min_idx] = A[min_idx], A[i] 
	endTime = datetime.datetime.now()
	#Printout
	print("Selection sort end")
	#print ("Posortowany ciąg:") 
	#for i in range(len(A)): 
	#	print(A[i])
	listOfResults.append("S;"+str(inputType)+";"+str(endTime-startTime))



#Insertion sort
def insertionSort(inputArray, inputType): 
	print("Insertion sort start")
	A = inputArray
	startTime = datetime.datetime.now()
	for i in range(1, len(A)): 
		key = A[i] 
		#Moving elements of A[0..i-1], which are greater that key, to one position ahead of their current position
		j = i-1
		while j >=0 and key < A[j] : 
				A[j+1] = A[j] 
				j -= 1
		A[j+1] = key
	endTime = datetime.datetime.now()
	print("Insertion sort end")
	#print("Insertion sort:")
	#for i in range(len(A)): 
	#	print (A[i]) 
	listOfResults.append("I;"+str(inputType)+";"+str(endTime-startTime))

#Merge sort
def mergeSort(inputArray, ifPrint = 0, inputType = "Z"):
	if ifPrint == 1:
		print("Merge sort start")
	A = inputArray
	startTime = datetime.datetime.now()
	if len(A) > 1:
		# Finding the mid of the array
		mid = len(A)//2
		# Dividing the array elements
		L = A[:mid]
		# into 2 halves
		R = A[mid:]
		# Sorting the first half
		mergeSort(L)
		# Sorting the second half
		mergeSort(R)
		i = j = k = 0
		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				A[k] = L[i]
				i += 1
			else:
				A[k] = R[j]
				j += 1
			k += 1
		# Checking if any element was left
		while i < len(L):
			A[k] = L[i]
			i += 1
			k += 1
		while j < len(R):
			A[k] = R[j]
			j += 1
			k += 1
	if ifPrint == 1:
		endTime = datetime.datetime.now()
		print("Merge sort end")
		#print("Merge sort:")
		for i in range(0, len(A)):
			#print(A[i])
			if (inputType == "R"):
				listSortedAsc.append(A[i])
		listOfResults.append("M;"+str(inputType)+";"+str(endTime-startTime))


selectionSort(listToBeSorted, "R")
insertionSort(listToBeSorted, "R")
mergeSort(listToBeSorted, 1, "R")

listSortedDesc = list(reversed(listSortedAsc))

selectionSort(listToBeSorted, "A")
insertionSort(listToBeSorted, "A")
mergeSort(listToBeSorted, 1, "A")

selectionSort(listToBeSorted, "D")
insertionSort(listToBeSorted, "D")
mergeSort(listToBeSorted, 1, "D")

print("posortowany ciąg ASC")
for i in range(len(listSortedAsc)):
	print(listSortedAsc[i])

print("posortowany ciąg DESC")
for i in range(len(listSortedDesc)):
	print(listSortedDesc[i])

print("Wyniki")
#Print results
for i in range(len(listOfResults)):
	print(listOfResults[i])