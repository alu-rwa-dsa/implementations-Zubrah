
list1 = ( 1, 50, 20, 40 ,"Mambo", 90, "Juma")
list2 = ("Mambo", 1, 50 , 20 , 23 , 90, 40, "Juma")


def Missing_element():
    print(set(list2).difference(list1))


Missing_element()