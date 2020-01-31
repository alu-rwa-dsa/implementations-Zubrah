# create  an empty list
list_final = [] 

#define the finction of lists
def lists_of_list(inputs):
    for i in inputs: 
        for j in i: 
            if j not in list_final: 
                list_final.append(j) 
    return list_final

    #list_merged = list(map(''.join, list_final))
    

inputs = [["g", "h", "a"], ["h", "z", "a"], ["g", "m", "z"]] 
  
# printing original list 
print("The original list is : " + str(inputs)) 
  
print("The String after duplicates removal is : ", lists_of_list(inputs)) 


""" for this algorithim we can see that the time complexity for running this algorithim would be O(n^2)
due to the existance of two  iterators while the space complexity is O(n) as number of elements in the lists"""
