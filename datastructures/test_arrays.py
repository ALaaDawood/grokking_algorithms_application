import unittest
from arrays import DynamicArray


class TestDynamicArray(unittest.TestCase):
    def setUp(self) -> None:
        self.arr = DynamicArray()

    def test_size(self):
        self.assertEqual(self.arr.size(), 0)

    def test_capacity(self):
        self.assertEqual(self.arr.capacity(), 1)

    def test_is_empty(self):
        self.assertEqual(self.arr.is_empty(), True)

    def test_get_item_by_index(self):
        self.arr.push(1)
        self.arr.push(20)
        self.arr.push(80)
        self.arr.push(5)
        self.assertEqual(self.arr.get_item_by_index(2), 80)
        with self.assertRaises(IndexError):
            self.arr.get_item_by_index(9)
        with self.assertRaises(IndexError):
            self.arr.get_item_by_index(-1)

    def test_push(self):
        self.arr.push(1)
        self.arr.push(20)
        self.assertEqual(self.arr.get_item_by_index(self.arr.size() - 1), 20)
        self.arr.push(80)
        self.arr.push(5)
        self.assertEqual(self.arr.get_item_by_index(self.arr.size() - 1), 5)

    def test_pop(self):
        self.arr.push(1)
        self.arr.push(20)
        self.assertEqual(self.arr.pop(), 20)
        self.arr.push(80)
        self.arr.push(5)
        self.assertEqual(self.arr.pop(), 5)
        self.assertEqual(self.arr.pop(), 80)
        self.assertEqual(self.arr.pop(), 1)
        self.assertEqual(self.arr.size(), 0)

    def test_find_item(self):
        self.arr.push(1)
        self.arr.push(20)
        self.arr.push(80)
        self.arr.push(5)
        self.assertEqual(self.arr.find_item(80), 2)
        self.assertEqual(self.arr.find_item(90), -1)

    def test_delete_by_index(self):
        self.arr.push(1)
        self.arr.push(20)
        self.arr.push(80)
        self.arr.push(5)
        self.arr.push(9)
        self.arr.delete_at_index(2)
        self.assertEqual(self.arr.size(), 4)
        self.assertEqual(self.arr.get_item_by_index(0), 1)
        self.assertEqual(self.arr.get_item_by_index(1), 20)
        self.assertEqual(self.arr.get_item_by_index(2), 5)
        self.assertEqual(self.arr.get_item_by_index(3), 9)
        with self.assertRaises(IndexError):
            self.arr.delete_at_index(7)

    def test_delete_by_value(self):
        self.arr.push(1)
        self.arr.push(20)
        self.arr.push(80)
        self.arr.push(5)
        self.arr.push(9)
        self.arr.push(80)
        self.arr.delete_value(80)
        self.assertEqual(self.arr.size(), 4)
        self.assertEqual(self.arr.get_item_by_index(0), 1)
        self.assertEqual(self.arr.get_item_by_index(1), 20)
        self.assertEqual(self.arr.get_item_by_index(2), 5)
        self.assertEqual(self.arr.get_item_by_index(3), 9)

    def test_insert_at_index(self):
        self.arr.push(1)
        self.arr.push(20)
        self.arr.push(80)
        self.arr.push(5)
        self.arr.insert_at_index(2, 9)
        self.assertEqual(self.arr.get_item_by_index(2), 9)
