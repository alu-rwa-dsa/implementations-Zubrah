
from Question3 import Dynamic_array
from Question3 import contains, insert, reverse

import unittest

var = Dynamic_Array([1, 2, 3])


class TestMyCase(unittest.TestCase):
    # test  for contains
    def test_contains(self):
        self.assertEqual(contains(var(1, 2, 3), 2), True)

    # test  for insert
    def test_insert(self):
        self.assertEqual(insert(var(1, 2, 3), 10, 1), [1, 10, 2, 3])

    # test  for reverse
    def test_reverse(self):
        self.assertEqual(reverse(var(1, 2, 3)), [3, 2, 1])

    # test  for contains when input is a string
    def test_case_four(self):
        self.assertEqual(contains(var(1, 2, 3), "f"), False)

    # test case for  Invalid Input
    def test_case_five(self):
        self.assertEqual(insert(Dynamic_array(1, 2, 3), "str", "st"), 'Invalid Input')


if __name__ == "__main__":
    unittest.main()
