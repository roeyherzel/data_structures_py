from pytest import fixture
from .bst import BST, find, find_min, find_max, find_height, find_successor


@fixture
def bst():
    bst = BST()
    bst.insert(10)
    yield bst

@fixture
def bst_full():
    bst = BST()
    bst.insert(15)
    bst.insert(10)
    bst.insert(20)
    bst.insert(8)
    bst.insert(12)
    bst.insert(17)
    bst.insert(25)
    bst.insert(4)
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


class TestDelete:
    def get_tree(self):
        bst = BST()
        for i in [12,5,15,3,7,13,17,1,9,14,20,8,11,18]:
            bst.insert(i)

        return bst

    def test_delete_leaf_node(self):
        bst = self.get_tree()

        parent = find(bst.root, 9)
        child = parent.left

        assert parent.left.data == 8
        assert parent.right.data == 11

        assert child.left is None
        assert child.right is None

        bst.delete(8)

        assert find(bst.root, 8) is None
        assert parent.left is None
        assert parent.right.data == 11

    def test_delete_node_with_one_child(self):
        bst = self.get_tree()

        parent = find(bst.root, 5)
        child = parent.left

        assert parent.left.data == 3
        assert parent.right.data == 7

        assert child.left.data == 1
        assert child.right is None

        bst.delete(3)

        assert find(bst.root, 3) is None
        assert parent.left.data == 1
        assert parent.right.data == 7

    def test_delete_node_with_two_children(self):
        bst = self.get_tree()

        parent = find(bst.root, 12)
        child = parent.right

        assert parent.left.data == 5
        assert parent.right.data == 15

        assert child.left.data == 13
        assert child.right.data == 17

        bst.delete(15)

        assert find(bst.root, 15) is None
        assert parent.left.data == 5
        assert parent.right.data == 17

def test_find_min(bst_full):
    assert find_min(bst_full.root).data == 4

def test_find_max(bst_full):
    assert find_max(bst_full.root).data == 25

def test_find_height(bst_full):
    assert find_height(bst_full.root) == 3


class TestFindSuccessor:
    def get_tree(self):
        bst = BST()
        for i in [12,5,15,3,7,13,17,1,9,14,20,8,11,18]:
            bst.insert(i)

        return bst

    def test_has_right_subtree(self):
        bst = self.get_tree()

        assert find_successor(bst.root, 9).data == 11
        assert find_successor(bst.root, 17).data == 18

    def test_no_right_subtree(self):
        bst = self.get_tree()

        assert find_successor(bst.root, 3).data == 5
        assert find_successor(bst.root, 8).data == 9
        assert find_successor(bst.root, 1).data == 3

    def test_no_successor(self):
        bst = self.get_tree()

        assert find_successor(bst.root, 20) is None