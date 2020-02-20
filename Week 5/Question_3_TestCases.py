import unittest
from Question_3 import *

# Assign a variable and pushing stack values to the Stack list
Implementation = Stack()
Implementation.push(5)
Implementation.push(7)
Implementation.push(8)
Implementation.push(1)
Implementation.push(10)


# Testing all the cases for primary methods
class MyTestStack(unittest.TestCase):
    # Test for Empty Stack
    def test_isEqual(self):
        self.assertEqual(Implementation.isEmpty(), False)

    # Test for size of Stack
    def test_isNotNone(self):
        self.assertEqual(Implementation.size(), 4)

    # Test for deleting from a Stack
    def test_deleting(self):
        self.assertEqual(Implementation.pop(), 10)

    # Test for pushing values from a Stack
    def test_pushing(self):
        self.assertIsNot(Implementation.push(5), 5)

    # Test for peeking an element from a Stack
    def test_peeking(self):
        self.assertEqual(Implementation.peek(), 1, msg="Code didn't work perfectly")

    # Test for re-checking the size of Stack after removal and additions
    def test_sizeofStack(self):
        self.assertEqual(Implementation.size(), 5)

    # Test for checking the Stack Property is its either empty or having elements
    def test_isNotEmpty(self):
        self.assertFalse(Implementation.isEmpty(), False)

    def test_top(self):
        self.assertEqual(Implementation.top(), 10)

    def test_top_case_2(self):
        self.assertIsNotNone(Implementation.top(), None)


if __name__ == '__main__':
    unittest.main()
