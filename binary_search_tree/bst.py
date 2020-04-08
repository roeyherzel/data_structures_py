from .node import Node

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = _insert(self.root, data)

    def search(self, data) -> bool:
        return find(self.root, data) is not None

    def delete(self, data):
        self.root = _delete(self.root, data)


def _insert(node, data):
    if not node:
        node = Node(data)

    elif data <= node.data:
        node.left = _insert(node.left, data)
    else:
        node.right = _insert(node.right, data)

    return node

def _delete(root: Node, data):
    if not root:
        return None

    # search left
    if root.data > data:
        root.left = _delete(root.left, data)

    # search right
    elif root.data < data:
        root.right = _delete(root.right, data)

    # found
    else:
        # no children
        if not root.left and not root.right:
            del root
            root = None

        # 1 child right
        elif not root.left:
            temp = root
            root = root.right
            del temp

        # 1 child left
        elif not root.right:
            temp = root
            root = root.left
            del temp

        # 2 children
        else:
            temp = find_min(root.right)
            root.data = temp.data
            root.right = _delete(root.right, temp.data)

    return root

def find(root: Node, data) -> Node:
    if not root:
        return None

    if root.data == data:
        return root

    if data <= root.data:
        return find(root.left, data)

    return find(root.right, data)

def find_min(root: Node) -> Node:
    """finds smallest node in the tree"""
    if not root:
        raise Exception('tree is empty')

    if not root.left:
        return root

    return find_min(root.left)

def find_max(root: Node) -> Node:
    """finds largest node in the tree"""
    if not root:
        raise Exception('tree is empty')

    if not root.right:
        return root

    return find_max(root.right)

def find_height(node: Node) -> int:
    """find the height of a given node in the tree"""
    if not node:
        return -1; # height of an empty tree

    return max(find_height(node.left), find_height(node.right)) + 1 # 1 edge from node to subtree

def find_successor(root: Node, data) -> Node:
    """find the next in-order node"""
    current = find(root, data)

    if not current:
        return None

    # Case 1: node has right subtree
    if current.right:
        return find_min(current.right)

    # Case 2: no right subtree
    else:
        successor = None
        ancessor = root

        while ancessor != current:
            if current.data < ancessor.data:
                successor = ancessor
                ancessor = ancessor.left
            else:
                ancessor = ancessor.right

    return successor


def find_predecessor(root: Node, data) -> Node:
    # TODO: find the previous in-order node
    pass