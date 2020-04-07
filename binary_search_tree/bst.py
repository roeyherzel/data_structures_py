from .node import Node

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = _insert(self.root, data)

    def search(self, data):
        return _search(self.root, data)

def _insert(node, data):
    if not node:
        node = Node(data)

    elif data <= node.data:
        node.left = _insert(node.left, data)
    else:
        node.right = _insert(node.right, data)

    return node

def _search(node, data):
    if not node:
        return False

    if node.data == data:
        return True

    if data <= node.data:
        return _search(node.left, data)

    return _search(node.right, data)


def find_min(self):
    # TODO
    raise NotImplemented

def find_max(self):
    # TODO
    raise NotImplemented

def find_height(node):
    # TODO
    raise NotImplemented