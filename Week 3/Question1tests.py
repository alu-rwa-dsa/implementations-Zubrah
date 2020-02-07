import unittest
from Question1 import My_SimpleArray


# define the Unit test class
class MyTestCase(unittest.TestCase):
    def test_isEqual(self):
        self.assertEqual(My_SimpleArray([1, 2, 3]).len(), 3)  # test for the length of an array

    def test_getMethod(self):
        self.assertEqual(My_SimpleArray([1, 2, 3]).get(2), 3)  # test for get method

    def test_setMethod(self):
        self.assertEqual(My_SimpleArray([1, 2, 3]).set(1), None)  # test for a set method


if __name__ == '__main__':
    unittest.main()
