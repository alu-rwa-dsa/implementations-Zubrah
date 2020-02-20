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

    def isEmpty(self):
        return self.head is None

    def insertFirst(self, data):
        newNode = Node(data)
        if self.head:
            self.head.setPrevious(newNode)
        newNode.setNext(self.head)
        self.head = newNode

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