#import a random module to enable random number generations
import random 
import timeit
#import matplotlib.pyplot as plt


#form a list with a random generated number

timelist = []
spacelist= []
list1 = [random.sample(range(100), i) for i in range(1, 101)]
# create a list with a range of value
for i in range(1, 10):
#     #sorted_list = sorted(list1)
# #use a pop method to get the maximum value
#     #sorted_list.pop()
    start = timeit.timeit()
    
    end = timeit.timeit()
    time_to_execute = end - start
    timelist.append(time_to_execute)
    print(timelist)
    
    

    


    





# # define the function to return maximum value
# def max(list1):
#     sorted_list = sorted(list1)
#     max = sorted_list.pop()
#     return max

# # print the maximum value of the random generated numbers
# print(max(list1))

