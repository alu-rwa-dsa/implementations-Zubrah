import unittest
from Question_1 import *

Implementations = OrderedList_Implementations()
Implementations.add(31)
Implementations.add(23)
Implementations.add(34)
Implementations.add(60)
Implementations.add(12)
Implementations.size()
Implementations.search(93)
Implementations.search(13)


class MyTestCase(unittest.TestCase):
    def test_Is_Size(self):
        self.assertEqual(Implementations.size(), 5)

    def test_search_func(self):
        self.assertEqual(Implementations.search(12), True)

    def test_IsEmpty(self):
        self.assertIs(Implementations.isEmpty(), False, msg="The list is not empty")

    def test_add(self):
        self.assertIs(Implementations.add(5), None, msg="A number five is added to the list")

    def test_retrieve_Node(self):
        self.assertFalse(Implementations.search(120), True)

    def test_IsEmpty_case2(self):
        self.assertFalse(Implementations.isEmpty(), False)

    def test_search_fun_case_2(self):
        self.assertIsNotNone(Implementations.search(12), True)

    def test_IsEmpty_case_3(self):
        self.assertIsNotNone(Implementations.isEmpty(), True)

    def test_size_case_2(self):
        self.assertIsNot(Implementations.size(), 90)

    def test_add_case_2(self):
        self.assertEquals(Implementations.add(67), None)


if __name__ == '__main__':
    unittest.main()
