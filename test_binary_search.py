
import unittest
from binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def setUp(self) -> None:
        self.sample_array = [1, 3, 5, 7, 9]  


    def test_binary_search_found_first_item(self):
        item = 1
        expected_index = 0
        self.assertEqual(binary_search(self.sample_array, item), expected_index)

    def test_binary_search_found_middle_item(self):
        item = 7
        expected_index = 3
        self.assertEqual(binary_search(self.sample_array, item), expected_index)
    
    def test_binary_search_found_last_item(self):
        item = 9
        expected_index = 4
        self.assertEqual(binary_search(self.sample_array, item), expected_index)

    def test_binary_search_item_not_found(self):
        item = 8
        self.assertEqual(binary_search(self.sample_array, item), None)
