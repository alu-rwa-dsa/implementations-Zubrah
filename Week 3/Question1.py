"""Time Complexity:
get method has O(1) as the return the new value as updated without storing any new info
len method has O(n) as we looking through all the elements
set method also have O(1) as we search for a specific index in an array

Space Complexity:
len method and get method both have O(1) due to the fact that have one instance variable
while set method will take O(n) if all  return type are taken into account if not will take O(1) as space Complexity

 """


# define a class for simple Array
class My_SimpleArray:
    def __init__(self, inputs):  # define the arguments and pass them to SimpleArray class
        self.UserInputs = inputs  # initialize the UserInputs

    # define the length method
    def len(self):
        # assign count to zero
        count = 0
        # loop through all the UserInputs
        for a in self.UserInputs:
            # add a count for each element in UserInputs
            count += 1
        # return a count
        return count

    # define a get method and return the UserInputs index
    def get(self, i):
        return self.UserInputs[i]

    # define a set method and pass a argument
    def set(self, value):
        # check for the value  if not greater than length of an array
        if value < self.len():
            # return the value
            self.UserInputs = value
