import random
import datetime


##############################Quick sort code
def quicksort(arr, start , stop, mode):
	if(start < stop):
		if mode == 1: #Random pivot
			pivotindex = partitionrand(arr,start, stop)
		if mode == 2: #First element as pivot
			pivotindex = partitionlow(arr,start, stop)
		if mode == 3: #Last element as pivot
			pivotindex = partitionhigh(arr,start, stop)
		quicksort(arr , start , pivotindex-1, mode)
		quicksort(arr, pivotindex + 1, stop, mode)

def partitionrand(arr , start, stop):
	randpivot = random.randrange(start, stop)

	arr[start], arr[randpivot] = arr[randpivot], arr[start]
	return partitionlow(arr, start, stop)

def partitionlow(arr,start,stop):
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

def partitionhigh(arr, start, stop): 
	i = (start - 1)
	pivot = arr[stop]
	for j in range(start, stop): 
		if arr[j] <= pivot:
			i = i+1
			arr[i], arr[j] = arr[j], arr[i] 
	arr[i+1], arr[stop] = arr[stop], arr[i+1]
	return (i+1) 

def quicksortengine(inputArray, quicksortmode = 1, inputType = "Z", ifSave = 0, saveResults = 0, measurePoint = 0):
    A = []
    for i in range(0, len(inputArray)):
        A.append(inputArray[i])
    startTime = datetime.datetime.now()
    quicksort(inputArray, 0, len(A) - 1,quicksortmode)
    endTime = datetime.datetime.now()
    if (ifSave == 1):
        for i in range(len(inputArray)):
            sortedArrayAsc.append(inputArray[i])
    if (saveResults == 1):
        resultsList.append("Q;"+str(quicksortmode)+";"+str(inputType)+";"+str(measurePoint)+";"+str(endTime-startTime))

##############################Merge Sort code
def mergeSort(alist):
	if len(alist)>1:
		mid = len(alist)//2
		lefthalf = alist[:mid]
		righthalf = alist[mid:]

		mergeSort(lefthalf)
		mergeSort(righthalf)

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

##############################Heap


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

#quicksortengine(inputArray = input, quicksortmode = 3, inputType = "R", ifSave = 1, saveResults = 1, measurePoint = 0)
mergeSortEngine(inputArray = input, inputType = "R", ifSave = 1, saveResults = 1, measurePoint = 0)
print ("Sorted array is:")
print(sortedArrayAsc)
print(randomArray)

print ("Results:")
print(resultsList)

