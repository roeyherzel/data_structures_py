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

        if not prev.next:
            raise IndexError(f'Could not find node at position {pos}')

        node.next = prev.next
        prev.next = node

    def delete(self, pos=1):
        # remove at beginning
        if pos <= 1:
            head = self.head.next
            self.head = head
            return

        # remove at n
        prev = self.head
        i=0
        while i < pos-2 and prev.next:
            prev = prev.next
            i = i+1

        if not prev.next:
            raise IndexError(f'Could not find node at position {pos}')

        curr = prev.next
        prev.next = curr.next

        del curr

    def reverse(self):
        prev = None
        node = self.head

        while node:
            _next = node.next
            node.next = prev

            prev = node
            node = _next

        self.head = prev

    def reverseV2(self):
        self.head = reversive(self.head)


def reversive(node):
    if not node.next:
        return node

    head = reversive(node.next)
    q = node.next
    q.next = node
    node.next = None

    return head