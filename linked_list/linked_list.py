from .node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        if not self.head:
            return 'LinkedList()'

        node = self.head
        data = str(node.data)

        while node.next:
            node = node.next
            data = f'{data} -> {node.data}'

        return f'LinkedList({data})'

    def insert(self, data, pos=1):
        node = Node(data)

        # insert head
        if self.head is None:
            self.head = node
            return

        # insert at beginning
        if pos <= 1:
            node.next = self.head
            self.head = node
            return

        # insert at n
        prev = self.head
        i=0
        while i < pos-2 and prev.next:
            prev = prev.next
            i = i+1

        node.next = prev.next
        prev.next = node

    def remove(self):
        pass

    def print(self):
        pass

    def reverse(self):
        pass