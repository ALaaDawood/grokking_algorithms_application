class Stack:
    def __init__(self) -> None:
        self.stack = []
        self._size = 0
        self._top = -1

    def create(self, size):
        self.stack = [None] * size
        self._size = size
        return self.stack

    def push(self, item):
        if(self.is_full()):
            raise IndexError("Stack is Full")
        self._top += 1
        self.stack[self._top] = item

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            element = self.stack[self._top]
            self.stack[self._top] = None
            self._top -= 1
            return element

    def is_empty(self):
        return self._top == -1

    def is_full(self):
        return self._top == self._size -1

    def peek(self):
        return self.stack[self._top]

    def size(self):
        return self._size
