# SelectionSort

Summary: The idea behind SelectionSort is to find the "smallest" member of your list at each iteration of the array.  This is not a high performing algorithm as it needs to look at all the data set at each iteration.  

Performance: O(n<sup>2</sup>)


![alt text][flowchart]

[flowchart]: SelectionSort.png "Algorithm Flowchart"

Sample Code:

```python
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
	
>>> print (SelectionSort([42, 10, 82, 99, 3, 5]))
[3, 5, 10, 42, 82, 99]
```
