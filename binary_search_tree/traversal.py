from queue import Queue


def level_order(root):
    """breath-first binary search tree traversal"""
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

