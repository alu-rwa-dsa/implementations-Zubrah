
"""
Time complexity of this solution is O(n). The solution is similar to pre-order traversal of Binary Tree.
"""
def isHeap(array_list):
    # will start from the root to the last item
    for i in range(int((len(array_list)- 2) / 2) + 1):

        # If left child is greater will return false
        if array_list[2 * i + 1] > array_list[i]:
            return False

        # If right child is greater will return false
        if (2 * i + 2 < len(array_list) and
                array_list[2 * i + 2] > array_list[i]):
            return False
    return True


if __name__ == '__main__':

    arr = [90, 15, 10, 7, 12, 2, 7, 3]

    isHeap(arr)
    print(isHeap(arr))

    # if isHeap(array_list=arr):
    #     print("Yes")
    # else:
    #     print("No")

