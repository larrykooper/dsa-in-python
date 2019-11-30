from src.queue.queue import Queue

class TestQueue:

    def test_enqueue(self):
        q = Queue()
        q.enqueue(9)
        assert q.count() == 1

    def test_enqueue_and_dequeue(self):
        q = Queue()
        q.enqueue(45)
        q.enqueue(99)
        res = q.dequeue()
        assert res == 45
        assert q.count() == 1

    def test_count(self):
        q = Queue()
        q.enqueue(3)
        q.enqueue(88)
        assert q.count() == 2

    def test_is_empty(self):
        q = Queue()
        q.enqueue(4)
        q.enqueue(8)
        res = q.dequeue()
        res = q.dequeue()
        assert q.is_empty

