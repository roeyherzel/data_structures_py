from .node import Node

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = insert(self.root, data)

    def search(self, data):
        return search(self.root, data)


def insert(node, data):
    if not node:
        node = Node(data)

    elif data <= node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)

    return node

def search(node, data):
    if not node:
        return False

    if node.data == data:
        return True

    if data <= node.data:
        return search(node.left, data)

    return search(node.right, data)