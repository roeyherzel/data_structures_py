from .node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        node.next = self.head
        self.head = node

    def remove(self):
        pass

    def print(self):
        pass

    def reverse(self):
        pass