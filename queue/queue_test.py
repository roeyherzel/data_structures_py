import pytest
from .queue import Queue


def test_init_queue():
    queue = Queue()

    assert queue.is_empty is True
    assert queue.peek() is None
    assert queue.front is None
    assert queue.rear is None

class TestEnqueue:
    def test_enqueue_first(self):
        queue = Queue()
        queue.enqueue(10)

        assert queue.is_empty is False
        assert queue.peek() == 10

    def test_enqueue_multi(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        assert queue.is_empty is False
        assert queue.peek() == 10

    def test_enqueue_after_dequeue_last(self):
        queue = Queue()
        queue.enqueue(10)
        queue.dequeue()
        queue.enqueue(20)

        assert queue.is_empty is False
        assert queue.peek() is 20

class TestDequeue:
    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        queue.dequeue()

        assert queue.is_empty is False
        assert queue.peek() is 20

        queue.dequeue()

        assert queue.is_empty is False
        assert queue.peek() is 30

    def test_dequeue_last(self):
        queue = Queue()
        queue.enqueue(10)
        queue.dequeue()

        assert queue.is_empty is True
        assert queue.peek() is None

    def test_dequeue_empty(self):
        queue = Queue()

        with pytest.raises(Exception):
            queue.dequeue()

        assert queue.is_empty is True
        assert queue.peek() is None