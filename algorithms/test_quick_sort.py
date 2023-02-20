import unittest
from algorithms.quick_sort import quick_sort

class TestQuickSort(unittest.TestCase):
    def test_sorting_unsorted_array(self):
        unsorted_arr = [10, 5, 20, 1, 15, 3]
        sorted_arr = [1, 3, 5, 10, 15, 20]
        self.assertSequenceEqual(quick_sort(unsorted_arr), sorted_arr)

    def test_sorting_sorted_array(self):
        unsorted_arr = [1, 3, 5, 10, 15, 20]
        sorted_arr = [1, 3, 5, 10, 15, 20]
        self.assertSequenceEqual(quick_sort(unsorted_arr), sorted_arr)

    def test_sorting_unsorted_array_with_duplicates(self):
        unsorted_arr = [10, 5, 20, 10, 1, 15, 3, 1]
        sorted_arr = [1, 1, 3, 5, 10, 10, 15, 20]
        self.assertSequenceEqual(quick_sort(unsorted_arr), sorted_arr)

    def test_sorting_sorted_array_with_duplicates(self):
        unsorted_arr = [1, 1, 3, 5, 10, 10, 15, 20]
        sorted_arr = [1, 1, 3, 5, 10, 10, 15, 20]
        self.assertSequenceEqual(quick_sort(unsorted_arr), sorted_arr)

    def test_sorting_one_item_array(self):
        unsorted_arr = [10]
        sorted_arr = [10]
        self.assertSequenceEqual(quick_sort(unsorted_arr), sorted_arr)

    def test_sorting_empty_array(self):
        unsorted_arr = []
        sorted_arr = []
        self.assertSequenceEqual(quick_sort(unsorted_arr), sorted_arr)

    def test_sorting_array_with_negative_values(self):
        unsorted_arr = [0, 2, -60, 51, 100, 7, 4, -3]
        sorted_arr = [-60, -3, 0, 2, 4, 7, 51, 100] 
        self.assertSequenceEqual(quick_sort(unsorted_arr), sorted_arr)
