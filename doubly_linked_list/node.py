
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        data_prev = self.prev.data if self.prev else None
        data_next = self.next.data if self.next else None

        return f"Node(data={self.data}, prev={data_prev}, next={data_next})"