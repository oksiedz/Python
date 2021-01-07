import random

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
	return partition(arr, start, stop)

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


array = [10, 7, 8, 9, 1, 5]
print("Input array:")
print(array)
quicksort(array, 0, len(array) - 1, 3)
print("Sorted array:")
print(array)
