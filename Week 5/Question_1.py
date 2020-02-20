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

        temp = Node(Node_Value)
        if previous is None:
            temp.set_Next_Node(self.head)
            self.head = temp
        else:
            temp.set_Next_Node(current)
            previous.set_Next_Node(temp)

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

print(Implementations.size())
print(Implementations.search(93))
print(Implementations.search(13))
