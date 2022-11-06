from collections import deque  


class Stack:
    def create(self):
        self.stack = deque()
        return self.stack

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if(self.is_empty()):
            raise IndexError("Stack is empty")
        else:
            return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)