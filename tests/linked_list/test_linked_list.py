from linked_list import LinkedList

class TestLinkedList:

    def test_insert_at_beginning(self):
        l = LinkedList()
        l.insert_at_beginning(10)
        assert l.count() == 1