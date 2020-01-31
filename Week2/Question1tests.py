import unittest

# Python3 code to demonstrate working of
# remove additional space from string
# Using re.sub()
import re


def removeSpace(name):
    return re.sub(' +', ' ', name)


inputs = removeSpace(name=" Ugali is       Mama")


# printing original string
# print("The Original String was ;", str(User_inputs))

# printing result
# print("The strings after extra space removal : " + str(inputs))


class MyTestCase(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(removeSpace(name="Ugali is       Mama"), "Ugali is Mama")

    def test_Is_not_Equal(self):
        self.assertIsNot(removeSpace(name="Ugali is       Mama"), "Ugali is       Mama")

    def test_is_not_None(self):
        self.assertIsNotNone(removeSpace(name="Ugali is       Mama"), "Ugali is       Mama")


if __name__ == '__main__':
    unittest.main()
