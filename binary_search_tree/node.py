
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        left = str(self.left.data) if self.left else None
        right = str(self.right.data) if self.right else None

        return f'Node(data={self.data}, left={left}, right={right})'