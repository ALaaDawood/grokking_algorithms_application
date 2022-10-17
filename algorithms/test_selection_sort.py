import unittest
from selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):
    def test_sorting_unsorted_array(self):
        unsorted_arr = [10, 5, 20, 1, 15, 3]
        sorted_arr = [1, 3, 5, 10, 15, 20]
        self.assertSequenceEqual(selection_sort(unsorted_arr), sorted_arr)

    def test_sorting_sorted_array(self):
        unsorted_arr = [1, 3, 5, 10, 15, 20]
        sorted_arr = [1, 3, 5, 10, 15, 20]
        self.assertSequenceEqual(selection_sort(unsorted_arr), sorted_arr)

    def test_sorting_unsorted_array_with_duplicates(self):
        unsorted_arr = [10, 5, 20, 10, 1, 15, 3, 1]
        sorted_arr = [1, 1, 3, 5, 10, 10, 15, 20]
        self.assertSequenceEqual(selection_sort(unsorted_arr), sorted_arr)

    def test_sorting_sorted_array_with_duplicates(self):
        unsorted_arr = [1, 1, 3, 5, 10, 10, 15, 20]
        sorted_arr = [1, 1, 3, 5, 10, 10, 15, 20]
        self.assertSequenceEqual(selection_sort(unsorted_arr), sorted_arr)
