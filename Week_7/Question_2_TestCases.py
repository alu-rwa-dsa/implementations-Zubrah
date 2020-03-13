import unittest
from Week_7.Question_2 import SpecialSort


class MyTestCase(unittest.TestCase):
    def test_alphanumeric(self):
        Implementation = {"carl": 40, "alan": 2, "bob": 1, "danny": 3, }
        self.assertEqual(SpecialSort(Implementation), None)

    def test_negative(self):
        test_2 = {1: 5, 20: -2, -1: 56, 45: -1, 22: 3}
        self.assertEqual(SpecialSort(test_2), None)

    def test_for_duplicate(self):
        test_3 = {4: -5, 3: -5, 7: -5, 6: -7, 10: -5}
        self.assertEqual(SpecialSort(test_3), None)


if __name__ == '__main__':
    unittest.main()
