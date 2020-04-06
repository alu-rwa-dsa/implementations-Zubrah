def heapify(arr, n, i):
    smallest = i  # Initialize smallest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # If left child is smaller than root
    if l < n and arr[l] < arr[smallest]:
        smallest = l

        # If right child is smaller than
    # smallest so far
    if r < n and arr[r] < arr[smallest]:
        smallest = r

        # If smallest is not root
    if smallest != i:
        (arr[i],
         arr[smallest]) = (arr[smallest],
                           arr[i])

        # Recursively heapify the affected
        # sub-tree
        heapify(arr, n, smallest)


def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    arr = [4, 6, 3, 2, 9]
    n = len(arr)
    printArray(arr, n)
