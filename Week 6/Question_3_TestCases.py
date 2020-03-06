import unittest
from Question_3 import *

Implementation = Fib(10)


class MyTestCase(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(Fib(10), 34)

    def test_Negative_Input(self):
        self.assertEqual(Fib(-10), None)

    def test_Greater_than_Number(self):
        self.assertGreater(Fib(10), 10)

    def test_not_none(self):
        self.assertIsNotNone(Fib(20), 12)

    def test_not_empty(self):
        self.assertIs(Fib(12), 89)


if __name__ == '__main__':
    unittest.main()
