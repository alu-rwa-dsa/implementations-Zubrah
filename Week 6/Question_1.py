# define Node class
class Node:
    def __init__(self, dataValues):
        self.dataValues = dataValues  # assign Data values
        self.next = None  # assign the next values as null


# create a Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_dataValue):
        new_node = Node(new_dataValue)
        new_node.next = self.head
        self.head = new_node

    def searching_value(self, val):
        current = self.head
        while current is not None:
            if current.dataValues == val:
                return True
            current = current.next
        return False


if __name__ == '__main__':
    searchValues = LinkedList()
    searchValues.push(5)
    searchValues.push(12)
    searchValues.push(23)
    searchValues.push(13)

    if searchValues.searching_value(21):
        print("Yes")
    else:
        print("No")



