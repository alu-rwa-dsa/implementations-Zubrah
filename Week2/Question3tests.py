import unittest

# create  an empty list
list_final = []


# define the finction of lists
def lists_of_list(inputs):
    for i in inputs:
        for j in i:
            if j not in list_final:
                list_final.append(j)
    return list_final

    # list_merged = list(map(''.join, list_final))


inputs = [["g", "h", "a"], ["h", "z", "a"], ["g", "m", "z"]]


# printing original list
# print("The original list is : " + str(inputs))

# print("The String after duplicates removal is : ", lists_of_list(inputs))


class MyTestCase(unittest.TestCase):
    def test_is_equal(self):
        self.assertEqual(lists_of_list(inputs), ['g', 'h', 'a', 'z', 'm'])

    def test_is_not_Equal(self):
        self.assertIsNot(lists_of_list(inputs), None)

    def test_is_Not_None(self):
        self.assertIsNotNone(lists_of_list(inputs), True)

    def test_is_almost_equal(self):
        self.assertListEqual(lists_of_list(inputs), ['g', 'h', 'a', 'z', 'm'])


if __name__ == '__main__':
    unittest.main()
