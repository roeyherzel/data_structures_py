from .traversal import in_order

def is_bst(root):
    values = in_order(root)

    for i in range(1, len(values)):
        if not values[i-1] <= values[i]:
            return False

    return True
