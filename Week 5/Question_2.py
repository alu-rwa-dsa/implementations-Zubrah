"""Time Complexity:
a) The Time complexity of insertion and deletion a value between the node is depends on the position
your going to insert or delete, when the position is in-front of the node the Time complexity will be
O(1) but if either between the node or at the end it will take O(n) time complexity.
b) The Time complexity to perform a search operation in both terms will take O(n)

Space Complexity:
a) The Space Complexity of insertion, deletion and searching will take O(1) in both terms as
no more memory is required to extend memory.
b) The Space complexity of adding, checking if empty or size of the linked list will take O(1)
as also they don't tend to add any memory.
"""


class Node(object):
    def __init__(self, data, Next=None, Previous=None):
        self.data = data
        self.next = Next
        self.previous = Previous

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

    def setPrevious(self, newPrevious):
        self.previous = newPrevious


class Doubly_Linked_List(object):
    def __init__(self):
        self.head = None

    # method to check if the Linked List is empty

    def isEmpty(self):
        return self.head is None

    # method to add data to the first Node

    def insertFirst(self, data):
        newNode = Node(data)
        if self.head:
            self.head.setPrevious(newNode)
        newNode.setNext(self.head)
        self.head = newNode

    # method to add data to the last Node

    def insertLast(self, data):
        newNode = Node(data)
        current = self.head
        while current.getNext() is not None:
            current = current.getNext()
        current.setNext(newNode)
        newNode.setPrevious(current)

    def getAllData(self):
        ''' This function displays the data elements of the Linked List '''
        current = self.head
        elements = []
        while current:
            elements.append(current.getData())
            current = current.getNext()

        return elements

    # method to remove an item from a linked list
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


if __name__ == '__main__':
    myList = Doubly_Linked_List()
    myList.insertFirst(1)
    myList.insertFirst(12)
    myList.insertFirst(32)
    myList.insertFirst(22)
    myList.insertLast(2)
    myList.remove(12)
    print(myList.getAllData())
