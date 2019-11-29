from stack import Stack

class TestStack:

    def test_push(self):
        s = Stack()
        s.push(17)
        assert s.count() == 1