def Search(arr, item):
    # assign the variables
    index = 0
    boolean = False
    # loop through the arr
    while index < len(arr) and not boolean:
        # check index if equal to the item if true return true otherwise false
        if arr[index] == item:
            boolean = True
        else:
            index = index + 1

    return boolean


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(Search(testlist, 3))
print(Search(testlist, 13))
