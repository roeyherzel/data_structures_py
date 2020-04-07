from pytest import fixture
from .bst import BST
from .traversal import level_order, pre_order, in_order, post_order


letters = ['F','D','J','B','E','G','K','A','C','I','H']

@fixture
def bst():
    bst = BST()
    for i in letters:
        bst.insert(i)

    yield bst


def test_level_order(bst):
    assert level_order(bst.root) == letters

def test_pre_order(bst):
    assert pre_order(bst.root) == ['F','D','B','A','C','E','J','G','I','H','K']

def test_in_order(bst):
    assert in_order(bst.root) == ['A','B','C','D','E','F','G','H','I','J','K']

def test_post_order(bst):
    assert post_order(bst.root) == ['A','C','B','E','D','H','I','G','K','J','F']
