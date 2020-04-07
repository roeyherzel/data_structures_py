from pytest import fixture

from .utils import is_bst
from .bst import BST

@fixture
def bst():
    bst = BST()
    for i in ['F','D','J','B','E','G','K','A','C','I','H']:
        bst.insert(i)

    yield bst


def test_is_bst_true(bst):
    assert is_bst(bst.root) is True


def test_is_bst_false(bst):
    bst.root.left = bst.root.right.right

    assert is_bst(bst.root) is False