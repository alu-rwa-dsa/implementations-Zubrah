"""
Time Complexity and Space Complexity:
The time Complexity to run the algorithm will be O(n) as it traverse through list array and assign labels to
root as the first index and create different subtrees.
ans the Space Complexity would be O(n) due to the fact that were printing and writing a new list with all subtrees
and root

"""


def exceptFirstColumn(data):
    if data and data[0]:
        return [row[1:] for row in data]
    else:
        return []


def exceptFirstLine(data):
    if data:
        return data[1:]


def left(data):
    # Returns the part of the data use to build the left subTree
    return exceptFirstColumn(data)


def right(data):
    # Returns the part of the data used to build the right subtree
    return exceptFirstColumn(exceptFirstLine(data))


class Node:
    def __init__(self, value):
        self.value = value

        self.leftChild = None
        self.rightChild = None

    def __repr__(self):
        if self.leftChild is not None and self.rightChild is not None:
            return "[{0} (L:{1} | R:{2}]".format(self.value, self.leftChild.__repr__(), self.rightChild.__repr__())
        else:
            return "[{0}]".format(self.value)


def fromData2Tree(data):
    if data and data[0]:
        node = Node(data[0][0])

        node.leftChild = fromData2Tree(left(data))
        node.rightChild = fromData2Tree(right(data))

        return node

    else:
        return None



