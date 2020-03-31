from .node import Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if not self.head:
            return ''

        node = self.head
        data_forward = str(node.data)

        while node.next:
            node = node.next
            data_forward = f'{data_forward}->{node.data}'

        data_backward = str(node.data)

        while node.prev:
            node = node.prev
            data_backward = f'{node.data}<-{data_backward}'

        return f'{data_forward}\n{data_backward}'


    def insert(self, data, index=0):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        # insert at beginning
        if index <= 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        # insert at index
        node = self.head
        i = 0
        while i < index-1 and node.next:
            node = node.next
            i = i+1

        next_n = node.next
        # next is None when index >= last node
        if next_n:
            next_n.prev = new_node

        node.next = new_node
        new_node.prev = node
        new_node.next = next_n

    def delete(self, index=0):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            return

        # delete at beginning
        if index <= 0:
            new_head = self.head.next
            new_head.prev = None
            self.head = new_head
            return

        # delete at index
        curr = self.head
        i=0
        while i < index and curr.next:
            curr = curr.next
            i = i + 1

        if i != index:
            raise IndexError('node index out of range')

        before = curr.prev
        after = curr.next

        before.next = after
        if after:
            after.prev = before

    def reverse(self):
        pass