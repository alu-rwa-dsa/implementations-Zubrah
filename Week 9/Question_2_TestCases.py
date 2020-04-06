import unittest
from Week_9.Question_2 import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr = [4, 6, 3, 2, 9]
        self.assertEqual(heapify(arr, len(arr), 0), None)


if __name__ == '__main__':
    unittest.main()
