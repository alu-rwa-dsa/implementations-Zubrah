# Time and Space Complexity:
"""The time Complexity for checking,
 a) isEmpty method  will be O(n) due to the fact it will check throughout all elements in the Stack list
 b) Push,pop and peek methods will take O(1) time complexity as it just push to the recent spot without passing through
  the whole code.
 c) The size method will take O(n) time complexity due to the factor that it has it has to pass and check all elements
  in a stack and returns the value of total number of elements.

  Space Complexity:
  a) The Empty and size method will take O(1) space complexity due to the factors that they don't add anything to
  the Stack but rather checking  elements
  b) The peek and pop method will take O(1) space complexity as it removes and peeks but doesn't require any addition
   of the structure of Stack
  c) The push method will take O(n) space complexity in a worst case scenario as it involves requiring an extra space
   every time adding an element to the Stack."""


# Defining a Stack Class
class Stack:
    # Initiating the Stack items in a list
    def __init__(self):
        self.stack_items = []

    # method for looking the empty stack
    def isEmpty(self):
        return self.stack_items == []

    # method for pushing an items to the Stack
    def push(self, stack_item):
        self.stack_items.append(stack_item)

    # method for popping out element from a Stack
    def pop(self):
        return self.stack_items.pop()

    # method for peeking(selecting) an element from a Stack
    def peek(self):
        return self.stack_items[len(self.stack_items) - 1]

    # method for checking the size of stack
    def size(self):
        return len(self.stack_items)


# create an object of the Stack class
Implement = Stack()
print(Implement.isEmpty())
Implement.push(5)
print(Implement.peek())
print(Implement.size())
print(Implement.stack_items)