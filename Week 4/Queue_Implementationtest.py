import unittest
from Queue import Queue

Implement = Queue()
Implement.enqueue(6)
Implement.enqueue("Hello")
Implement.enqueue("Zubrah")
Implement.enqueue("Buddah")
Implement.enqueue(20)
Implement.enqueue(67)


class QueueImplementationsCases(unittest.TestCase):
    # Testing for list property and status
    def test_isEqual(self):
        self.assertEqual(Implement.isEmpty(), False)

    #  Testing to check the size of queue
    def test_isNotNone(self):
        self.assertEqual(Implement.size(), 5)

    # Testing for deleting an element
    def test_deleting(self):
        self.assertEqual(Implement.dequeue(), 6)

    # Testing adding element to the queue
    def test_pushing(self):
        self.assertIsNot(Implement.enqueue(5), 5)

    # Testing for selecting an element from a queue
    def test_peeking(self):
        self.assertIs(Implement.dequeue(), "Hello", msg="Code worked perfectly")

    # Testing for looking the size of the queue
    def test_sizeofStack(self):
        self.assertEqual(Implement.size(), 5)

    # Testing to look for size of queue after additions and removal
    def test_isNotEmpty(self):
        self.assertFalse(Implement.isEmpty(), False)


if __name__ == '__main__':
    unittest.main()
