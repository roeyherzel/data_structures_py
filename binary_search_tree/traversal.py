from queue import Queue


def level_order(root):
    """breath-first tree traversal"""
    if not root:
        raise Exception('tree is empty')

    queue = Queue()
    output = []

    queue.enqueue(root)

    while not queue.is_empty:
        node = queue.dequeue()

        if node.left:
            queue.enqueue(node.left)

        if node.right:
            queue.enqueue(node.right)

        output.append(node.data)

    return output

def pre_order(root, output=[]):
    """depth-first DLR binary search tree traversal"""
    if not root:
        return output

    output.append(root.data)
    output = pre_order(root.left, output)
    output = pre_order(root.right, output)

    return output

def in_order(root, output=[]):
    """depth-first LDR tree traversal"""
    if not root:
        return output

    output = in_order(root.left, output)
    output.append(root.data)
    output = in_order(root.right, output)

    return output

def post_order(root, output=[]):
    """depth-first LRD tree traversal"""
    if not root:
        return output

    output = post_order(root.left, output)
    output = post_order(root.right, output)
    output.append(root.data)

    return output