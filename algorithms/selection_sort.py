def selection_sort(unsorted_arr):
    sorted_arr = []
    for i in range(len(unsorted_arr)):
        smallest = find_smallest(unsorted_arr)
        sorted_arr.append(unsorted_arr.pop(smallest))
    return sorted_arr


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
