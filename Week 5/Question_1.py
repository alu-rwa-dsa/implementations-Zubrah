"""
Time Complexity:
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


class Node:
    def __init__(self, Linked_list):
        self.data = Linked_list
        self.next = None

    def retrieve_Node(self):
        return self.data

    def retrieve_Next_Node(self):
        return self.next

    def set_Data_Node(self, new_data_Node):
        self.data = new_data_Node

    def set_Next_Node(self, new_next):
        self.next = new_next


class OrderedList_Implementations:
    def __init__(self):
        self.head = None

    def search(self, Node_Value):
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.retrieve_Node() == Node_Value:
                found = True
            else:
                if current.retrieve_Node() > Node_Value:
                    stop = True
                else:
                    current = current.retrieve_Next_Node()

        return found

    def add(self, Node_Value):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.retrieve_Node() > Node_Value:
                stop = True
            else:
                previous = current
                current = current.retrieve_Next_Node()

        var = Node(Node_Value)
        if previous is None:
            var.set_Next_Node(self.head)
            self.head = var
        else:
            var.set_Next_Node(current)
            previous.set_Next_Node(var)

    def isEmpty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.retrieve_Next_Node()

        return count


Implementations = OrderedList_Implementations()
Implementations.add(31)
Implementations.add(120)

print(Implementations.size())
print(Implementations.search(93))
print(Implementations.search(13))
