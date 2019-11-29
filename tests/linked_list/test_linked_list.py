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


    def test_search_when_not_found(self):
        l = LinkedList()
        l.insert_at_beginning(10)
        l.insert_at_beginning(20)
        result = l.search(15)
        assert result is None

    def test_search_when_found(self):
        l = LinkedList()
        l.insert_at_beginning(10)
        l.insert_at_beginning(20)
        result = l.search(10)
        assert result == 10
