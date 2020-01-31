import unittest
from Question5 import repeating_int

class TestStringMethods(unittest.TestCase):
    def test_int(self):
        number1 = repeating_int(5)
        self.assertEqual(repeating_int.addNumber(5,6), 13)






if __name__ == '__main__':
    unittest.main()