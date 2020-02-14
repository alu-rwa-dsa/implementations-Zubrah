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


class Queue:
    # initiating Queue items
    def __init__(self):
        self.Queue_items = []

    # making a new queue to the item/adding an item
    def enqueue(self, Queue_item):
        self.Queue_items.insert(0, Queue_item)

    # method for checking Queue status if empty or not
    def isEmpty(self):
        return self.Queue_items == []

    # method for removing element from a queue
    def dequeue(self):
        return self.Queue_items.pop()

    # method for checking the size of the queue
    def size(self):
        return len(self.Queue_items)


# Creating an object of the queue
Implement = Queue()
Implement.enqueue(6)
Implement.enqueue("Hello")
Implement.enqueue("Zubrah")
print(Implement.isEmpty())
print(Implement.size())
