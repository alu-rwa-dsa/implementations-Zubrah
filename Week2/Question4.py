
list1 = ( 1, 50, 20, 40 ,"Mambo", 90, "Juma")
list2 = ("Mambo", 1, 50 , 20 , 23 , 90, 40, "Juma")


def Missing_element():
    print(set(list2).difference(list1))


Missing_element()

""" For this algorithim the time complexity to run would be O(n) as it passes through all elements checking 
in the lists while the space complexity is O(1) as it checks without adding anything to memory"""