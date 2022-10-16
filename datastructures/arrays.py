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
        for i in range(len(self._arr)):
            if self._arr[i] == item:
                return i
        return -1
