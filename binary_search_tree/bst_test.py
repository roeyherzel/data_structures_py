from pytest import fixture
from .bst import BST


@fixture
def bst():
    bst = BST()
    bst.insert(10)
    yield bst


class TestGeneral:
    def test_root_init_as_none(self):
        assert BST().root is None

class TestInsert:
    def test_insert_empty_tree(self):
        bst = BST()
        bst.insert(10)

        assert bst.root.data == 10
        assert bst.root.left is None
        assert bst.root.right is None

    def test_insert_lesser(self, bst):
        bst.insert(5)

        assert bst.root.left.data == 5
        assert bst.root.right is None

        assert bst.root.left.left is None
        assert bst.root.left.right is None

    def test_insert_equal(self, bst):
        bst.insert(10)

        assert bst.root.left.data == 10
        assert bst.root.right is None

        assert bst.root.left.left is None
        assert bst.root.left.right is None

    def test_insert_greater(self, bst):
        bst.insert(15)

        assert bst.root.right.data == 15
        assert bst.root.left is None

        assert bst.root.right.left is None
        assert bst.root.right.right is None

class TestSearch:
    def test_search_empty_tree(self):
        assert BST().search(10) is False

    def test_search_single_node(self, bst):
        assert bst.search(10) is True
        assert bst.search(11) is False

    def test_search_lesser(self, bst):
        bst.insert(5)
        bst.insert(15)

        assert bst.search(5) is True
        assert bst.search(6) is False

    def test_search_greater(self, bst):
        bst.insert(5)
        bst.insert(15)

        assert bst.search(15) is True
        assert bst.search(6) is False
