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


def find_min(root):
    """finds smallest data in the tree"""
    if not root:
        raise Exception('tree is empty')

    if not root.left:
        return root.data

    return find_min(root.left)

def find_max(root):
    """finds largest data in the tree"""
    if not root:
        raise Exception('tree is empty')

    if not root.right:
        return root.data

    return find_max(root.right)

def find_height(node):
    """find the height of a given node in the tree"""
    if not node:
        return -1; # height of an empty tree

    return max(find_height(node.left), find_height(node.right)) + 1 # 1 edge from node to subtree