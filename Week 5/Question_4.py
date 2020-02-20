# Queue operations using doubly linked list

# Time and Space Complexity:
"""The time Complexity for checking,
 a) Enqueue method  will be O(1) as it only adds the element at the end of the queue without passing through all the
 elements.
 b) isEmpty method  will be O(n) due to the fact it will check throughout all elements in the Queue list
 b) Dequeue methods will take O(n) time complexity as it just remove to the first in element through passing
  the whole queue list.
 c) The size method will take O(n) time complexity due to the factor that it has it has to pass and check all elements
  in a stack and returns the value of total number of elements.

  Space Complexity:
  a) The Empty and size method will take O(1) space complexity due to the factors that they don't add anything to
  the Stack but rather checking  elements
  b) The enqueue and dequeue method will take O(1) space complexity as it removes and adds of the structure of Stack."""

# Node class

class Node:
    def __init__(self, Doubly_Linked_List):
        self.data = Doubly_Linked_List
        self.next = None
        self.prev = None


# Queue class contains a Node object

class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    # Function to add element to Queue
    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last.next.prev = self.last
            self.last = self.last.next

    # Function to remove an element to Queue

    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

    # Function/Method to return First element in the queue

    def first(self):
        return self.head.data

    # Method to return the size of the queue

    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

    # method to check the queue if Empty

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False


if __name__ == '__main__':
    Implementation = Queue()
    # Implementation.enqueue(3)
    Implementation.dequeue()
    Implementation.isEmpty()
