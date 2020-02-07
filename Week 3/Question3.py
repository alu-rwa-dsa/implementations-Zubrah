
"""The time complexity:
contains will has O(n) due to the fact that were looking for through all the elements
insert function also have O(n) due to fact inserting an element at the beginning will result to shifting of every element
reverse func has O(n) as we loop through every element

Space Complexity:
contains has o(1) space complexity while insert and reverse has o(n) as they return a new list
"""

from Question2 import Dynamic_Array


# define the contains function
def contains(array, value):
    for a in range(array.len()):
        if array.get(a) == value:
            return True
    return "The value is available"


# define the reverse func
def reverse(array):
    new_list = []
    for i in range(array.UserInputs.len(-1, -1, -1)):
        new_list.append(a)
    return new_list


# define a insert value func
def insert(array, val, i):
    random = 0
    array.add(random)
    for a in range(array.len(-1, i - 1, -1)):
        array.UserInputs[a] = array.UserInputs[a - 1]
    array.UserInputs[a] = val


var = Dynamic_Array([1, 2, 3])
print(contains(var, 2))
