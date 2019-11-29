from src.stack.stack import Stack

class TestStack:

    def test_push(self):
        s = Stack()
        s.push(17)
        assert s.count() == 1

    def test_pop(self):
        s = Stack()
        s.push(23)
        s.push(22)
        val = s.pop()
        assert val == 22

    def test_pop_underflow(self):
        s = Stack()
        val = s.pop()
        assert val is None

    def test_count(self):
        s = Stack()
        s.push(23)
        s.push(22)
        s.push(104)
        assert s.count() == 3

