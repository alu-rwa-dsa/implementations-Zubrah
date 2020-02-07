import _ctypes
import unittest

import array


# array_element = array.array('i', [1, 2, 3, 10, 14, 25, 7])


class SimpleArray(object):
    array_element = array.array('i', [1, 2, 3, 10, 14, 25, 7])

    def __init__(self, array_element):
        self.arr = array_element
        self.count = 0
        self.capacity = 1

    def __len__(self):
        count = 0
        for i in self.array_element:
            count = count + 1
        return count

    def __getitem__(self, i):
        if not 0 <= i < self.array_element:
            return IndexError("Item is out of bounds")
        return i

    def __set__(self, instance, value):
        var = self[value]
        return var


SimpleArray(object)


class MyUnitTest(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(SimpleArray(object), 'i', [1, 2, 3, 10, 14, 25, 7])

    def test_IsNot(self):
        self.assertIsNot(SimpleArray(object), 'i', [1, 2, 3, 10, 14, 25, 7])

    def test_IsNotNone(self):
        self.assertIsNotNone(SimpleArray(object), 'i')
