def quick_sort(unsorted_arr):
    if len(unsorted_arr) < 2:
        return unsorted_arr
    pivot = unsorted_arr[0]
    smaller = [i for i in unsorted_arr[1:] if i <= pivot]
    greater = [i for i in unsorted_arr[1:] if i > pivot]
    return quick_sort(smaller) + [pivot] + quick_sort(greater)
