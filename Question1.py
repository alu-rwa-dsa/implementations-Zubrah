#Author : Zubery Msemo
#AIM: Implement a measure to track time by using different algorithims
#Import a timeit module to track time
import timeit

#Include all the code to test inside the triple qoutes
#Sample 1: create a  variable and store storing the code we want to test here i used for loop
test1 = """
a = range(1000)
b = []
for i in a:
    b.append(i*2)
"""
#Call the time.timeit() function. The timeit() function will get the test code as an argument,
#executes it and records the execution time. To get an accurate time, I ordered timeit() to perform 10 cycles. 
# Therefore, I had to divide the output by 10 to get the execution time for only one cycle.
time_to_execute = timeit.timeit(test1, number=10)/10

#print the executed time
print("The time to execute the first test is " , time_to_execute)


# Sample 2:here we repeated the above test using a list and multiplying the items of another list

test2 = """
a = range(1000)
b = [i*2 for i in a]
"""
elapsed_time1 = timeit.timeit(test2, number=10)/10
print("The time to the execute the second test is : " , elapsed_time1)
