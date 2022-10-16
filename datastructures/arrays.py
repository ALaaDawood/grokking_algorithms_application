class DynamicArray:
    def __init__(self) -> None:
        self._capacity = 1
        self._size = 0
        self._arr = self.make_array(self._capacity)

    def make_array(self, capacity):
        return [None] * capacity

    def _extend(self):
        self._capacity *= 2

    def _shrink(self):
        self._capacity = int(self._capacity / 2)

    def _expand_array(self):
        self._extend()
        newarr = self.make_array(self._capacity)
        for i in range(len(self._arr)):
            newarr[i] = self._arr[i]
        self._arr = newarr

    def size(self) -> int:
        return self._size

    def capacity(self) -> int:
        return self._capacity

    def get_item_by_index(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("index is out of bounds")
        return self._arr[index]

    def _len(self):
        return self._size

    def is_empty(self):
        if self._size == 0:
            return True
        return False

    def push(self, value):
        if self._size == self._capacity:
            self._expand_array()
        self._arr[self._size] = value
        self._size += 1

    def pop(self):
        self._size -= 1
        if self._size == self._capacity / 2:
            self._shrink()
        return self._arr[self._size]

    def find_item(self, item):
        for i in range(self._len()):
            if self._arr[i] == item:
                return i
        return -1

    def delete_at_index(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("index is out of bounds")
        self.shift_left_at_index(index)
        self._size -= 1
        if self._size == self._capacity / 2:
            self._shrink()

    def delete_value(self, value):
        for i in range(self._len()):
            if self._arr[i] == value:
                self.shift_left_at_index(i)
                self._size -= 1
                if self._size == self._capacity / 2:
                    self._shrink()

    def shift_left_at_index(self, index):
        for i in range(index, self._size):
            self._arr[i] = self._arr[i + 1]

    def shift_right_at_index(self, index):
         for i in range(self._size, index, -1):
            self._arr[i] = self._arr[i - 1]

    def insert_at_index(self, index, item):
        if self._size == self._capacity:
            self._expand_array()
        self.shift_right_at_index(index)
        self._arr[index] = item
