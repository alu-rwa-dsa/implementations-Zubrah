import unittest
from Question2 import Dynamic_Array

var = Dynamic_Array([1, 2, 3])


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(var.add(9), [1, 2, 3, 9])  # test for a add method

    def test_delecting(self):
        self.assertEqual(var.dele(), [1, 2, 3])  # test fro a del method


if __name__ == '__main__':
    unittest.main()
