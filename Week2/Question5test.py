import unittest


def repeating_int(num):
    for num in range(num + 1):
        for i in range(num):
            print(num, end=" ")


repeating_int(4)


class MyTestCase(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(repeating_int(6), None)

    def test_is_not_Equal(self):
        self.assertIsNot(repeating_int(4), 4)

    def test_is_a_negative_int(self):
        self.assertEqual(repeating_int(-7), None)

    def test_is_not_num(self):
        self.assertIsNot(repeating_int(6), 8)

    def test_for_negative(self):
        self.assertFalse(repeating_int(10),  False)


if __name__ == '__main__':
    unittest.main()
