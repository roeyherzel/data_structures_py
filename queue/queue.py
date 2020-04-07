from .node import Node

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def __str__(self):
        if self.is_empty:
            return 'Queue(empty)'

        return f'Queue(front={self.front.data}, rear={self.rear.data})'

    def enqueue(self, data):
        node = Node(data)

        if not self.front and not self.rear:
            self.front = self.rear = node
            return

        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.is_empty:
            raise Exception("queue is empty")

        data = self.front.data
        self.front = self.front.next
        return data

    @property
    def is_empty(self):
        return self.front is None

    def peek(self):
        if self.is_empty:
            return None

        return self.front.data