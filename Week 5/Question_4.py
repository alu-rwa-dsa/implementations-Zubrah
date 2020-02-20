# Queue operations using doubly linked list

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
