import unittest
from Week_8.Question_5 import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        m = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        self.assertEqual(process(m), None)

    def test_Case_2(self):
        n = [10.5, 3, 11.25, 17, 6.75, 7, 19,
             23.5, 14, 19.75, 12, 4, 1, 5.5]
        self.assertEqual(process(n), None)

    def test_Case_3(self):
        z = [-15, -13, 11, 17, 5, 7, 19,
             25, 4, 1, 12, 4, 1, 9]
        self.assertEqual(process(z), None)

    def test_Case_4(self):
        a = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        self.assertEqual(process(a), None)


if __name__ == '__main__':
    unittest.main()
