
"""Time Complexity:
add and del method has O(1) as it takes uniform time to add an element and del an element

Space Complexity:
add and removing an element has O(n) as it return a list which as the list grows it will grow larger and larger"""



from Question1 import My_SimpleArray


class Dynamic_Array(My_SimpleArray):
    def __init__(self, Inputs):
        super().__init__(Inputs)

    def add(self, value):
        self.UserInputs.append(value)
        output = []
        for a in self.UserInputs:
            output.append(a)
        return output

    def dele(self):
        self.UserInputs.pop()
        new_list = []
        for a in self.UserInputs:
            new_list.append(a)
        return new_list


var = Dynamic_Array([1, 2, 3])
# print(var.add(6))
#
# print(var.dele())
