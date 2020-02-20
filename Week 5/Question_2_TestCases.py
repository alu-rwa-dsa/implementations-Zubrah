import unittest
from Question_2 import *

myList = Doubly_Linked_List()
myList.insertFirst(1)
myList.insertFirst(12)
myList.insertFirst(32)
myList.insertFirst(22)
myList.insertLast(2)
myList.remove(12)
print(myList.getAllData())


class MyTestCase(unittest.TestCase):
    def test_Insert_First(self):
        self.assertEqual(myList.insertFirst(6), None)

    def test_Insert_Last(self):
        self.assertEqual(myList.insertLast(12), None)

    def test_IsEmpty(self):
        self.assertIs(myList.isEmpty(), False, msg="The list is not empty")

    def test_get_all_Data(self):
        self.assertEqual(myList.getAllData(), [6, 22, 32, 1, 2, 12, 67], msg="Couldn't get all data")

    def test_remove_Node(self):
        self.assertFalse(myList.remove(1), True)

    def test_IsEmpty_case2(self):
        self.assertFalse(myList.isEmpty(), False)

    def test_insert_first_case_2(self):
        self.assertEquals(myList.insertFirst(12), None)

    def test_Insert_Last_2(self):
        self.assertNotEqual(myList.insertLast(67), True)

    def test_remove_case_2(self):
        self.assertIsNot(myList.remove(22), 90)

    def test_add_case_2(self):
        self.assertIsNot(myList.getAllData(), [1, 34, 5, 7, 8])


if __name__ == '__main__':
    unittest.main()
