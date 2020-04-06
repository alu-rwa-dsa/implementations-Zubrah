"""
 Time complexity for Building a Binary Heap is O(n). as building a heapify is O(n) and sorting is O(log n) as
 taking the greatest runtime will be O(n).
 The space complexity of searching an element in heap is O (n) and other operations that require traversing through
 all elements will take O(n)
"""


class BinaryHeap:
    # constructor
    def __init__(self):
        self.items = []

    # size of the heap
    def size(self):
        return len(self.items)

    # parent method
    def parent(self, i):
        return (i - 1) // 2

    # getting the left node
    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    # get the items of the heap
    def get(self, i):
        return self.items[i]

    # get the maximum value of heap
    def get_max(self):
        if self.size() == 0:
            return None
        return self.items[0]

    def get_min(self):
        if self.size() == 0:
            return None
        return self.items[-1]

    def extract_min(self):
        if self.size() == 0:
            return None
        smallest = self.get_min()
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.max_heapify(0)
        return smallest

    # extract the maximum value from the heap
    def extract_max(self):
        if self.size() == 0:
            return None
        largest = self.get_max()
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.max_heapify(0)
        return largest

    # define the maximum heapify method
    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l <= self.size() - 1 and self.get(l) > self.get(i):
            largest = l
        else:
            largest = i
        if r <= self.size() - 1 and self.get(r) > self.get(largest):
            largest = r
        if largest != i:
            self.swap(largest, i)
            self.max_heapify(largest)

    # swap the items
    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    # inserting the item in a heap
    def insert(self, key):
        index = self.size()
        self.items.append(key)

        while index != 0:
            p = self.parent(index)
            if self.get(p) < self.get(index):
                self.swap(p, index)
            index = p
