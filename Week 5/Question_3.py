# Stack implementation using singly Linked lIst
# create a Node class
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


class Node:
    def __init__(self, Linked_List_Data):
        self.data = Linked_List_Data
        self.next = None
        self.prev = None


# create a class Stack with Linked list Object

class Stack:
    def __init__(self, ):
        self.head = None

    # method to add element to the stack

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    # method to remove an element from a stack
    def pop(self):
        if self.isEmpty():
            return None
        else:
            Node_to_Pop = self.head
            self.head = self.head.next
            Node_to_Pop.next = None
            return Node_to_Pop.data
        # if self.head is None:
        #     return None
        # else:
        #     temp = self.head.data
        #     self.head = self.head.next
        #     self.head.prev = None
        #     return temp

    # method to return an top element of the Stack
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data

    def top(self):
        return self.head.data

    # method to return the size of the Stack
    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

    # method to check Stack if empty

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False


if __name__ == '__main__':
    Implementation = Stack()
    Implementation.push(4)
    # print(Implementation.pop())
    # print(Implementation.peek())
    # print(Implementation.size())
