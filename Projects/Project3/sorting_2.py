import random
import datetime

##############################Quick sort code
def quickSort(arr, start , stop, mode):
	if(start < stop):
		if mode == 1: #Random pivot
			pivotindex = partitionRand(arr,start, stop)
		if mode == 2: #First element as pivot
			pivotindex = partitionLow(arr,start, stop)
		if mode == 3: #Last element as pivot
			pivotindex = partitionHigh(arr,start, stop)
		quickSort(arr , start , pivotindex-1, mode)
		quickSort(arr, pivotindex + 1, stop, mode)

def partitionRand(arr , start, stop):
	randpivot = random.randrange(start, stop)

	arr[start], arr[randpivot] = arr[randpivot], arr[start]
	return partitionLow(arr, start, stop)

def partitionLow(arr,start,stop):
	pivot = start
	i = start + 1
	for j in range(start + 1, stop + 1):
		if arr[j] <= arr[pivot]:
			arr[i] , arr[j] = arr[j] , arr[i]
			i = i + 1
	arr[pivot] , arr[i - 1] =\
			arr[i - 1] , arr[pivot]
	pivot = i - 1
	return (pivot)

def partitionHigh(arr, start, stop): 
	i = (start - 1)
	pivot = arr[stop]
	for j in range(start, stop): 
		if arr[j] <= pivot:
			i = i+1
			arr[i], arr[j] = arr[j], arr[i] 
	arr[i+1], arr[stop] = arr[stop], arr[i+1]
	return (i+1) 

def quickSortEngine(inputArray, quickSortMode = 1, inputType = "Z", ifSave = 0, saveResults = 0, measurePoint = 0):
    A = []
    for i in range(0, len(inputArray)):
        A.append(inputArray[i])
    startTime = datetime.datetime.now()
    quickSort(inputArray, 0, len(A) - 1, quickSortMode)
    endTime = datetime.datetime.now()
    if (ifSave == 1):
        for i in range(len(inputArray)):
            sortedArrayAsc.append(inputArray[i])
    if (saveResults == 1):
        resultsList.append("Q;"+str(quickSortMode)+";"+str(inputType)+";"+str(measurePoint)+";"+str(endTime-startTime))

##############################Merge Sort code
def mergeSort(alist):
	if len(alist)>1:
		mid = len(alist)//2
		leftHalf = alist[:mid]
		rightHalf = alist[mid:]

		mergeSort(leftHalf)
		mergeSort(rightHalf)

		i=0
		j=0
		k=0
		while i < len(leftHalf) and j < len(rightHalf):
			if leftHalf[i] <= rightHalf[j]:
				alist[k]=leftHalf[i]
				i=i+1
			else:
				alist[k]=rightHalf[j]
				j=j+1
			k=k+1

		while i < len(leftHalf):
			alist[k]=leftHalf[i]
			i=i+1
			k=k+1

		while j < len(rightHalf):
			alist[k]=rightHalf[j]
			j=j+1
			k=k+1

def mergeSortEngine(inputArray, inputType = "Z", ifSave = 0, saveResults = 0, measurePoint = 0):
	A = []
	for i in range(0, len(inputArray)):
		A.append(inputArray[i])
	#print("Start - Merge sort")
	startTime = datetime.datetime.now()
	mergeSort(A)
	endTime = datetime.datetime.now()
	#print("End - Merge sort")
	if (ifSave == 1):
		for i in range(len(A)):
			sortedArrayAsc.append(A[i])
	if (saveResults == 1):
		resultsList.append("M;"+str(inputType)+";"+str(measurePoint)+";"+str(endTime-startTime))

##############################HeapSort
def heapify(arr, n, i):
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2

	if l < n and arr[largest] < arr[l]:
		largest = l
	if r < n and arr[largest] < arr[r]:
		largest = r
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, n, largest)

def heapSort(arr):
	n = len(arr)

	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)

	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr, i, 0)

def heapSortEngine(inputArray, inputType = "Z", ifSave = 0, saveResults = 0, measurePoint = 0):
	A = []
	for i in range(0, len(inputArray)):
		A.append(inputArray[i])
	#print("Start - Heap sort")
	startTime = datetime.datetime.now()
	heapSort(A)
	endTime = datetime.datetime.now()
	#print("End - Heap sort")
	if (ifSave == 1):
		for i in range(len(A)):
			sortedArrayAsc.append(A[i])
	if (saveResults == 1):
		resultsList.append("H;"+str(inputType)+";"+str(measurePoint)+";"+str(endTime-startTime))

################################Working code
resultsList = []
sortedArrayAsc = []
sortedArrayDesc = []
input = []
randomArray = []
noOfGeneratedNumber = 10

print("Start of random array generation")
for i in range(0, noOfGeneratedNumber):
	randomArray.append(float(random.random()))
print("End of random array generation")


for i in range(0, len(randomArray)):
        input.append(randomArray[i])

print ("Input array is:")
print(randomArray)

quickSortEngine(inputArray = input, quickSortMode = 3, inputType = "R", ifSave = 1, saveResults = 1, measurePoint = 0)
#mergeSortEngine(inputArray = input, inputType = "R", ifSave = 1, saveResults = 1, measurePoint = 0)
#heapSortEngine(inputArray = input, inputType = "R", ifSave = 1, saveResults = 1, measurePoint = 0)
print ("Sorted array is:")
print(sortedArrayAsc)
print(randomArray)

print ("Results:")
print(resultsList)

