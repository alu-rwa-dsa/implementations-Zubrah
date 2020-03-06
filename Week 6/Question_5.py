def BinarySearch(array, val):

    # check fro the len of array and return false if zero
    if len(array) == 0:
        return False
    else:
        # assign a temp mid value to check for number
        mid_interval = len(array) // 2
        # if number found return true
        if array[mid_interval] == val:
            return True
        else:
            # if less than mid interval of left and re-do the function recursively
            if val < array[mid_interval]:
                return BinarySearch(array[:mid_interval], val)
            else:
                # if greater than mid interval re-do the function recursively focusing on right
                return BinarySearch(array[mid_interval + 1:], val)


list_to_test = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(BinarySearch(list_to_test, 30))

