
import random
import datetime

#Arrays to be used - randomArray - array with random numbers, sortedArrayAsc - array with sorted ascending numbers, sortedArrayDesc - array with sorted ascending numbers
randomArray = []
sortedArrayAsc = []
sortedArrayDesc = []

#variables explanation:
#inputArray - parameter for input array to be sorted
#ifSave = parameter set 1 if as an output there should be saved the sorted array
#inputType = parameter defining type of input array - if it's random (R), sorted ASC (A) or sorted DESC (D)
resultsList = []

#noOfGeneratedNumber - how many items contain array of random numbers
noOfGeneratedNumber = 17000

#print("Start of random array generation")
for i in range(0, noOfGeneratedNumber):
    randomArray.append(float(random.random()))
#print("End of random array generation")

#print("random array:")
#for i in range(len(randomArray)):
#    print(randomArray[i])

#Selection sort
def selectionSort(inputArray, ifSave = 0, inputType = "Z"):
	#Array to be sorted
	A = []
	for i in range(0, len(inputArray)):
		A.append(inputArray[i])
	#print("Start - Selection sort")
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
#	print("End - Selection sort")
	if (ifSave == 1):
		for i in range(len(A)):
			sortedArrayAsc.append(A[i])
	resultsList.append("S;"+str(inputType)+";"+str(endTime-startTime))

#Insertion sort
def insertionSort(inputArray, inputType = "Z"): 
#	print("Start - Insertion sort")
	A = []
	for i in range(0, len(inputArray)):
		A.append(inputArray[i])
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
#	print("End - Insertion sort")
	resultsList.append("I;"+str(inputType)+";"+str(endTime-startTime))

def mergeSort(inputArray, ifPrint = 0, inputType = "Z"):
#	if ifPrint == 1:
#		print("Merge sort start")
	A = []
	for i in range(0, len(inputArray)):
		A.append(inputArray[i])
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
#		print("End - Merge sort")
		resultsList.append("M;"+str(inputType)+";"+str(endTime-startTime))

print("Start - random sorting")
selectionSort(randomArray, 1, "R")
#insertionSort(randomArray, "R")
mergeSort(randomArray, 1, "R")
print("End - random sorting")

for i in range(0, len(sortedArrayAsc)):
	sortedArrayDesc.append(list(reversed(sortedArrayAsc))[i])

print("Start - sortedASC sorting")
#selectionSort(sortedArrayAsc, 0, "A")
insertionSort(sortedArrayAsc, "A")
mergeSort(sortedArrayAsc, 1, "A")
print("End - sortedASC sorting")
print("Start - sortedDESC sorting")
#selectionSort(sortedArrayDesc, 0, "D")
#insertionSort(sortedArrayDesc, "D")
mergeSort(sortedArrayDesc, 1, "D")
print("End - sortedDESC sorting")

#print("random array:")
#for i in range(0, len(randomArray)):
#	print(randomArray[i])

#print("sorted ASC array:")
#for i in range(0, len(sortedArrayAsc)):
#	print(sortedArrayAsc[i])

#print("sorted DESC array:")
#for i in range(0, len(sortedArrayDesc)):
#	print(sortedArrayDesc[i])

print("time results")
for i in range(0, len(resultsList)):
	print(resultsList[i])