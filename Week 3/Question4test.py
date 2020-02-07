from Question4 import Associative_list
import unittest

alist_for_test = Associative_list()
alist_for_test2 = Associative_list()
alist_for_test.add("Zubrah", 10)
alist_for_test2.add("Zubrah", 1000)


class TestMyCase(unittest.TestCase):
    # test  for add
    def test_add(self):
        self.assertEqual(alist_for_test.add("zubrah", 200), 'Not initialized as required')

    # test  for remove
    def test_remove(self):
        self.assertEqual(alist_for_test.remove("Zubrah"), 'Not initialized as required')

    # test  for modify
    def test_modify(self):
        self.assertEqual(alist_for_test2.modify("Zubrah", 500), 'Not initialized as required')

    # test  for lookup
    def test_lookup(self):
        self.assertEqual(alist_for_test.lookup("Zubrah"), 'Not initialized as required')


if __name__ == "__main__":
    unittest.main()
