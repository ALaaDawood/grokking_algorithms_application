import unittest

from datastructures.stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()
    
    def test_create_stack_with_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.create(5)
        self.assertEqual(self.stack.size(), 5)

    def test_push(self):
        self.stack.create(3)
        self.stack.push(4)
        self.assertEqual(self.stack.peek(), 4)
        self.stack.push(9)
        self.assertEqual(self.stack.peek(), 9)

    def test_pushing_into_full_stack(self):
        self.stack.create(2)
        self.stack.push(4)
        self.assertEqual(self.stack.peek(), 4)
        self.stack.push(9)
        self.assertEqual(self.stack.peek(), 9)
        with self.assertRaises(IndexError):
            self.stack.push(5)

    def test_pop(self):
        self.stack.create(3)
        self.stack.push(4)
        self.stack.push(9)
        self.assertEqual(self.stack.pop(), 9)
        self.assertEqual(self.stack.pop(), 4)

    def test_pop_from_empty_stack(self):
        self.stack.create(1)
        self.stack.push(4)
        self.assertEqual(self.stack.pop(), 4)
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_is_empty(self):
        self.stack.create(2)
        self.assertTrue(self.stack.is_empty())
        self.stack.push(5)
        self.assertFalse(self.stack.is_empty())

    def test_is_full(self):
        self.stack.create(2)
        self.assertFalse(self.stack.is_full())
        self.stack.push(5)
        self.stack.push(9)
        self.assertTrue(self.stack.is_full())
    
    def test_peek_returns_last_element_without_removing_it(self):
        self.stack.create(2)
        self.stack.push(9)
        self.assertEqual(self.stack.peek(), 9)
        self.assertFalse(self.stack.is_empty())