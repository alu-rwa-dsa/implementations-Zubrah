
# Python3 code to demonstrate working of 
# remove additional space from string 
# Using re.sub() 
import re 

def removeSpace(name) :
    return re.sub(' +', ' ', name) 
  

User_inputs = "Enter     a                    string"
inputs = removeSpace(User_inputs)
# printing original string  
print("The Original String was ;" , str(User_inputs))
  

# printing result  
print("The strings after extra space removal : " + str(inputs))