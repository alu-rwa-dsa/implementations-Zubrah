import unittest

list1 = (1, 50, 20, 40, "Mambo", 90, "Juma")
list2 = ("Mambo", 1, 50, 20, 23, 90, 40, "Juma")


def Missing_element():
    print(set(list2).difference(list1))


Missing_element()


class MyTestCase(unittest.TestCase):
    def test_Equal(self):
        self.assertEqual(Missing_element(), None)

    def test_Is_Not_Equal(self):
        self.assertIsNot(Missing_element(), 13)

    def test_number_of_elements(self):
        self.assertEqual(Missing_element(), None)

    def test_is_None(self):
        self.assertIsNone(Missing_element(), True)

    def test_is_False(self):
        self.assertFalse(Missing_element(), True)


if __name__ == '__main__':
    unittest.main()
