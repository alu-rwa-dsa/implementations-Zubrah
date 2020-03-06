import unittest
from Question_2 import *

Implementation = findingGCD(12, 24)


class MyTestCase(unittest.TestCase):
    # test fro true values
    def test_true(self):
        self.assertEqual(findingGCD(15, 625), 5)

    # test with one as GCD
    def test_with_one_as_GCD(self):
        self.assertEqual(findingGCD(12, 13), 1)

    # test large number
    def test_large(self):
        self.assertEqual(findingGCD(10000, 150000), 10000)

    def test_Zero_number(self):
        self.assertNotEqual(findingGCD(45, 0), 12)

    def test_Negative(self):
        self.assertEqual(findingGCD(-4, -8), None)

    def test_One_Negative(self):
        self.assertEqual(findingGCD(-4, 8), 4)


if __name__ == '__main__':
    unittest.main()
