# Binary Search

**Summary:**
The idea behind BinarySearch is to guess a value in the array, if the guessed index returns a value that is smaller than the desired value than you eleminate everything that is lower than the guessed index.  
If you guess the midpoint index at every run then you will elminate half the values each run.  You keep on repeating this process until you find the desired value.

_Assumption_: a key assumption to use Binary Search is that you are providing a sorted array.  If the array is not sorted then you cannot use this algorithm

**Flow Chart**

![alt text][flowchart]

[flowchart]: BinarySearch.png "Algorithm Flowchart"

**Sample Code**
```python

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

>>> sorted_array = [3, 5, 10, 42, 82, 99]

>>> (print binary_search(sorted_array, 10))
2

>>> (print binary_search(sorted_array, 17))
-1
```