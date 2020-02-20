import unittest
from Question_4 import *

Implementation = Queue()
Implementation.enqueue(6)
Implementation.enqueue("Hello")
Implementation.enqueue("Zubrah")
Implementation.enqueue("Buddah")
Implementation.enqueue(20)
Implementation.enqueue(67)


class QueueImplementationsCases(unittest.TestCase):
    # Testing for list property and status
    def test_isEqual(self):
        self.assertEqual(Implementation.isEmpty(), False)

    #  Testing to check the size of queue
    def test_isNotNone(self):
        self.assertEqual(Implementation.size(), 5)

    # Testing for deleting an element
    def test_deleting(self):
        self.assertEqual(Implementation.dequeue(), 6)

    # Testing adding element to the queue
    def test_pushing(self):
        self.assertIsNot(Implementation.enqueue(5), 5)

    # Testing for selecting an element from a queue
    def test_peeking(self):
        self.assertIs(Implementation.dequeue(), "Hello", msg="Code didn't work perfectly")

    # Testing for looking the size of the queue
    def test_sizeofStack(self):
        self.assertEqual(Implementation.size(), 5)

    # Testing to look for size of queue after additions and removal
    def test_isNotEmpty(self):
        self.assertFalse(Implementation.isEmpty(), False)


if __name__ == '__main__':
    unittest.main()
