import unittest

from datastructures.linked_lists import LinkedList


class TestLinkedLists(unittest.TestCase):
    def setUp(self) -> None:
        self.list = LinkedList()

    def test_add_back(self):
        self.assertEqual(self.list.size(), 0)
        self.list.add_back(1)
        self.assertEqual(self.list.size(), 1)
        self.list.add_back(2)
        self.assertEqual(self.list.size(), 2)
        self.assertEqual(self.list.get_last(), 2)

    def test_add_front(self):
        self.assertEqual(self.list.size(), 0)
        self.list.add_front(1)
        self.assertEqual(self.list.size(), 1)
        self.assertEqual(self.list.get_first(), 1)
        self.list.add_front(2)
        self.assertEqual(self.list.size(), 2)
        self.assertEqual(self.list.get_first(), 2)

    def test_delete(self):
        self.assertEqual(self.list.size(), 0)
        self.list.add_back(10)
        self.list.add_back(20)
        self.list.add_back(30)
        self.assertEqual(self.list.size(), 3)
        self.list.delete(10)
        self.assertEqual(self.list.size(), 2)
        self.assertEqual(self.list.get_first(), 20)

    def test_size(self):
        self.assertEqual(self.list.size(), 0)
        self.list.add_back(1)
        self.list.add_back(2)
        self.assertEqual(self.list.size(), 2)
        self.list.add_front(3)
        self.list.add_front(4)
        self.assertEqual(self.list.size(), 4)



