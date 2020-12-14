
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
noOfGeneratedNumber = 18000

#print("Start of random array generation")
for i in range(0, noOfGeneratedNumber):
    randomArray.append(float(random.random()))
#print("End of random array generation")

#print("random array:")
#for i in range(len(randomArray)):
#    print(randomArray[i])

#Selection sort
def selectionSort(inputArray, inputType = "Z"):
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
	resultsList.append("S;"+str(inputType)+";"+str(endTime-startTime))

#Insertion sort
def insertionSort(inputArray, inputType = "Z", ifSave = 0): 
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
	if (ifSave == 1):
		for i in range(len(A)):
			sortedArrayAsc.append(A[i])
	resultsList.append("I;"+str(inputType)+";"+str(endTime-startTime))

def mergeSortEngine(alist):
	if len(alist)>1:
		mid = len(alist)//2
		lefthalf = alist[:mid]
		righthalf = alist[mid:]

		mergeSortEngine(lefthalf)
		mergeSortEngine(righthalf)

		i=0
		j=0
		k=0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] <= righthalf[j]:
				alist[k]=lefthalf[i]
				i=i+1
			else:
				alist[k]=righthalf[j]
				j=j+1
			k=k+1

		while i < len(lefthalf):
			alist[k]=lefthalf[i]
			i=i+1
			k=k+1

		while j < len(righthalf):
			alist[k]=righthalf[j]
			j=j+1
			k=k+1

def mergeSort(inputArray, inputType = "Z", ifSave = 0):
	A = []
	for i in range(0, len(inputArray)):
		A.append(inputArray[i])
	#print("Start - Merge sort")
	startTime = datetime.datetime.now()
	mergeSortEngine(A)
	endTime = datetime.datetime.now()
	#print("End - Merge sort")
	if (ifSave == 1):
		for i in range(len(A)):
			sortedArrayAsc.append(A[i])
	resultsList.append("M;"+str(inputType)+";"+str(endTime-startTime))


print("Start - random sorting")
selectionSort(randomArray, "R")
insertionSort(randomArray, "R")
mergeSort(randomArray, "R", 1)
print("End - random sorting")

print("Start - Sorting Desc")
reverseStart = datetime.datetime.now()
#for i in range(0, len(sortedArrayAsc)):
#	sortedArrayDesc.append(list(reversed(sortedArrayAsc))[i])
sortedArrayDesc = list(reversed(sortedArrayAsc))
reverseEnd = datetime.datetime.now()
print("End - Sorting Desc, lasted: "+str(reverseEnd - reverseStart))

#print("sortowany DESC")
#print(sortedArrayDesc)
#sortedArrayDesc = list(reversed(sortedArrayAsc))

print("Start - sortedASC sorting")
selectionSort(sortedArrayAsc, "A")
insertionSort(sortedArrayAsc, "A")
mergeSort(sortedArrayAsc, "A", 0)
print("End - sortedASC sorting")
print("Start - sortedDESC sorting")
selectionSort(sortedArrayDesc, "D")
insertionSort(sortedArrayDesc, "D")
mergeSort(sortedArrayDesc, "D", 0)
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