from .bst import BST
from .traversal import level_order


def test_level_order():
    letters = ['F','D','J','B','E','G','K','A','C','I','H']
    bst = BST()

    for i in letters:
        bst.insert(i)

    assert level_order(bst.root) == letters