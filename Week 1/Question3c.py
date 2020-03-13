# An algorithim to sort out all int in a list using inbuilt method

# creating empty list
list1 = []

# asking number of elements to put in list
number_of_integers = int(input("Enter number of elements in list: "))

# iterating till num to append int in list
for i in range(1, number_of_integers + 1):

    # ask the user for inputs
    integers = int(
        input("Input an interger and press Enter for the next one: "))

    # append to the list and sort in ascending order
    list1.append(integers)

list2 = sorted(list1)

# print the sorted list
print(list2)
