# QuickSort

**Summary:**
QuickSort is a more efficient sorting algorithm than [SelectionSort](../SelectionSort).  

The intution behind Quicksort is:
1. pick a pivot point which is what will divide the array
2. place all elements in the array that are smaller in an array to the "left"
3. place all elements in the array that are larger in an array to the "right"
4. repeat step 1 for each array in 2. and 3. until each array is empty or has one element


**Performance:**
* best case: O(n log n)
* worst case: O(n<sup>2</sup>)

The average is typically the best case <i><b>if you always choose a pivot randomlly</b></i>


**Sample Code**

```python
# Counting down to 0
def quicksort(arr):
    if (len(arr) < 2):
        return arr
    else:
        # this is the pivot case
        pivot = arr[0]

        # sub-array of elements less than pivot
        smaller = [i for i in arr[1:] if i <= pivot]

        # sub-array of elements greater than pivot
        larger = [i for i in arr[1:] if i > pivot]

        return quicksort(smaller) + [pivot] + quicksort(larger)

>>> quicksort ([42, 10, 82, 99, 3, 5])
[3, 5, 10, 42, 82, 99]
```