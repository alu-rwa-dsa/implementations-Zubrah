def bubble_sort(list_to_sort):
    # Swap the elements to arrange in order
    for iter_num in range(len(list_to_sort) - 1, 0, -1):
        for idx in range(iter_num):
            if list_to_sort[idx] > list_to_sort[idx + 1]:
                temp = list_to_sort[idx]
                list_to_sort[idx] = list_to_sort[idx + 1]
                list_to_sort[idx + 1] = temp
    return list_to_sort


list_to_sort = [19, 2, 31, 45, 6, 11, 121, 27]
Implementation = bubble_sort(list_to_sort)

print(Implementation)
