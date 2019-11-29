from linked_list import LinkedList

class TestLinkedList:

    def test_insert_at_beginning(self):
        l = LinkedList()
        l.insert_at_beginning(10)
        assert l.count() == 1


    def test_remove_from_beginning(self):
        l = LinkedList()
        l.insert_at_beginning(20)
        value = l.remove_from_beginning()
        assert value == 20