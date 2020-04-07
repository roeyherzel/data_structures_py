from .node import Node

class Stack:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.is_empty:
            return 'Stack(empty)'

        return f'Stack(top={self.head.data})'

    def push(self, data):
        node = Node(data)

        if self.is_empty:
            self.head = node
            return

        node.next = self.head
        self.head = node

    def pop(self):
        if self.is_empty:
            raise Exception('stack is empty')

        data = self.head.data
        self.head = self.head.next

        return data

    def top(self):
        if self.is_empty:
            return None

        return self.head.data

    @property
    def is_empty(self):
        return self.head is None