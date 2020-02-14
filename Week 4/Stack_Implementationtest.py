# Importing a unitests and main class of the Stack
import unittest
from Stack_Implementation import Stack

# Assign a variable and pushing stack values to the Stack list
Implement = Stack()
Implement.push(5)
Implement.push(7)
Implement.push(8)
Implement.push(1)


# Testing all the cases for primary methods
class MyTestStack(unittest.TestCase):
    # Test for Empty Stack
    def test_isEqual(self):
        self.assertEqual(Implement.isEmpty(), False)

    # Test for size of Stack
    def test_isNotNone(self):
        self.assertEqual(Implement.size(), 3)

    # Test for deleting from a Stack
    def test_deleting(self):
        self.assertEqual(Implement.pop(), 1)

    # Test for pushing values from a Stack
    def test_pushing(self):
        self.assertIsNot(Implement.push(5), 5)

    # Test for peeking an element from a Stack
    def test_peeking(self):
        self.assertIs(Implement.peek(), 8, msg="Code worked perfectly")

    # Test for re-checking the size of Stack after removal and additions
    def test_sizeofStack(self):
        self.assertEqual(Implement.size(), 4)

    # Test for checking the Stack Property is its either empty or having elements
    def test_isNotEmpty(self):
        self.assertFalse(Implement.isEmpty(), False)


if __name__ == '__main__':
    unittest.main()
