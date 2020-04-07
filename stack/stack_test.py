import pytest
from .stack import Stack

def test_init():
    stack = Stack()

    assert stack.is_empty is True
    assert stack.head is None
    assert stack.top() is None


class TestPush:
    def test_push_to_empty_stack(self):
        stack = Stack()
        stack.push(10)

        assert stack.is_empty is False
        assert stack.top() == 10

    def test_push_multi_to_stack(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)

        assert stack.is_empty is False
        assert stack.top() == 30

class TestPop:
    def test_pop(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        data = stack.pop()

        assert data == 20
        assert stack.is_empty is False
        assert stack.top() == 10

    def test_pop_last(self):
        stack = Stack()
        stack.push(10)
        data = stack.pop()

        assert data == 10
        assert stack.is_empty is True
        assert stack.top() is None

    def test_pop_empty(self):
        stack = Stack()

        with pytest.raises(Exception):
            data = stack.pop()

        assert stack.is_empty is True
        assert stack.top() is None