
"""
Heap Sort has O(nlogn) time complexities for all the cases ( best case, average case and worst case).
"""


# heapify
def heapify(arr, n, i):
    largest = i  # largest value
    l = 2 * i + 1  # left
    r = 2 * i + 2  # right
    # if left child exists
    if l < n and arr[i] < arr[l]:
        largest = l
    # if right child exits
    if r < n and arr[largest] < arr[r]:
        largest = r
    # root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        # root.
        heapify(arr, n, largest)


# sort
def heapSort(arr):
    n = len(arr)
    # max-heap
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    # element extraction
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


# main

