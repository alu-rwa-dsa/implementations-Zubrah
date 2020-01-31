
list_to_add = []
# defining a repeating pattern of integers
def repeating_int(value):
    for i in range(value + 1):
        for j in range(i):
            list_to_add.append(i)    
    print(list_to_add)
    return list_to_add


repeating_int(value= 5) 


""" From this code it can be clearly seen that the time complexity to run the algorithim is O(n ^2) 
while the space complexity  is also O(n^2) """
