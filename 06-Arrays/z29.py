# Python program for implementation of Bubble Sort
arr = [64, 34, 25, 12, 22, 11, 90]
def bubbleSort(arr):
	for i in range(len(arr)-1):
		for j in range(0, len(arr)-i-1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]	
bubbleSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
	print("% d" % arr[i], end=" ")
