class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def size(self):
        if not self.head:
            return 0
        current_node = self.head
        size = 1
        while current_node.next:
            size += 1
            current_node = current_node.next
        return size

    def add_back(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def add_front(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        temp_node = self.head
        self.head = new_node
        new_node.next = temp_node

    def delete(self, value):
        if not self.head:
            return None
        if self.head.value == value:
            self.head = self.head.next
        current_node = self.head
        while current_node.next:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def get_first(self):
        return self.head.value

    def get_last(self):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        return current_node.value


l = LinkedList()
l.head = Node(3)
