# binary Search function, needs a sorted array
def binary_search (arr, item):
    min_val = 0
    max_val = len(arr) - 1

    while (min_val <= max_val):
        mid = (min_val + max_val)//2
        guess = arr[mid]
        if (guess == item):
            return mid
        if (guess > item):
            max_val = mid - 1
        else:
            min_val = mid + 1
    return -1

# To find the smallest value in the array provided
def getMinimum(arr):
	min_value = arr[0]
	min_idx = 0
	for i in range(1, len(arr)):
		if (arr[i] < min_value):
			min_value = arr[i]
			min_idx = i
	return min_idx
	
# The calling function which does the SelectionSort
def SelectionSort(arr):
	new_arr = []
	for i in range(len(arr)):
		min_idx = getMinimum(arr)
		new_arr.append(arr.pop(min_idx))
	return new_arr