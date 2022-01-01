# QuickSort

**Summary:**
QuickSort is a more efficient sorting algorithm than [SelectionSort](../SelectionSort).
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