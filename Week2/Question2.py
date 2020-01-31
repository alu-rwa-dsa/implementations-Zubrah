# Author: Zubery Msemo


# Create a empty list
frequency_of_string = {} 

#def the function to calculate the occurance of Strings
def Occurance_of_String(name):

# iterate the inputs to count the occurance of each string
    for i in Inputs:
        if i in frequency_of_string:
             frequency_of_string[i] += 1
        else:
            frequency_of_string[i] = 1 

# User Inputs
Inputs = input("Your String; ")
Occurance_of_String(Inputs)
  

  
# printing result  
print ("Count of all characters in your String is :\n " +  str(frequency_of_string))