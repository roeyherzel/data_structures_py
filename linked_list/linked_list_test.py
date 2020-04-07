import pytest
from .linked_list import LinkedList

def test_init_empty_head():
    ll = LinkedList()

    assert ll.head is None

class TestInsert:
    def test_insert_head(self):
        ll = LinkedList()
        ll.insert(10)

        assert ll.head.data == 10
        assert ll.head.next is None

    def test_insert_at_beginning(self):
        ll = LinkedList()
        ll.insert(10)
        ll.insert(20)

        assert ll.head.data == 20
        assert ll.head.next.data == 10
        assert ll.head.next.next is None

    def test_insert_at_n(self):
        ll = LinkedList()
        ll.insert(10)
        ll.insert(20)
        ll.insert(30)
        ll.insert(40, 2)

        assert ll.head.data == 30
        assert ll.head.next.data == 20
        assert ll.head.next.next.data == 40
        assert ll.head.next.next.next.data == 10
        assert ll.head.next.next.next.next is None

    def test_insert_at_ending(self):
        ll = LinkedList()
        ll.insert(10)
        ll.insert(20)
        ll.insert(30)
        ll.insert(40, 3)

        assert ll.head.data == 30
        assert ll.head.next.data == 20
        assert ll.head.next.next.data == 10
        assert ll.head.next.next.next.data == 40
        assert ll.head.next.next.next.next is None

class TestDelete:
    def test_delete_head(self):
        ll = LinkedList()
        ll.insert(10)
        ll.delete()

        assert ll.head is None

    def test_delete_at_beginning(self):
        ll = LinkedList()
        ll.insert(10)
        ll.insert(20)
        ll.delete()

        assert ll.head.data == 10
        assert ll.head.next is None

    def test_delete_at_n(self):
        ll = LinkedList()
        ll.insert(10)
        ll.insert(20)
        ll.insert(30)
        ll.delete(1)

        assert ll.head.data == 30
        assert ll.head.next.data == 10
        assert ll.head.next.next is None

    def test_delete_at_ending(self):
        ll = LinkedList()
        ll.insert(10)
        ll.insert(20)
        ll.insert(30)
        ll.delete(2)

        assert ll.head.data == 30
        assert ll.head.next.data == 20
        assert ll.head.next.next is None

    def test_delete_index_out_of_range(self):
        ll = LinkedList()
        ll.insert(10)

        with pytest.raises(IndexError):
            ll.delete(1)

class TestReverse:
    def test_reverse_iterative(self):
        ll = LinkedList()
        ll.insert(10)
        ll.insert(20)
        ll.insert(30)
        ll.reverse()

        assert ll.head.data == 10
        assert ll.head.next.data == 20
        assert ll.head.next.next.data == 30
        assert ll.head.next.next.next is None

    def test_reverse_recursive(self):
        ll = LinkedList()
        ll.insert(10)
        ll.insert(20)
        ll.insert(30)
        ll.reverseV2()

        assert ll.head.data == 10
        assert ll.head.next.data == 20
        assert ll.head.next.next.data == 30
        assert ll.head.next.next.next is None
