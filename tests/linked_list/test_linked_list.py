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

    def test_remove_from_beginning_when_empty(self):
        l = LinkedList()
        value = l.remove_from_beginning()
        assert value is None


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


    def test_delete_key_in_middle(self):
        l = LinkedList()
        l.insert_at_beginning(8)
        l.insert_at_beginning(7)
        l.insert_at_beginning(4)
        l.insert_at_beginning(9)
        l.insert_at_beginning(3)
        res = l.delete_key(4)
        assert res == 4
        assert l.count() == 4

    def test_delete_key_not_found(self):
        l = LinkedList()
        l.insert_at_beginning(4)
        l.insert_at_beginning(9)
        l.insert_at_beginning(3)
        res = l.delete_key(17)
        assert res is None

    def test_delete_key_at_beginning(self):
        l = LinkedList()
        l.insert_at_beginning(4)
        l.insert_at_beginning(9)
        l.insert_at_beginning(3)
        res = l.delete_key(3)
        assert res == 3
        assert l.count() == 2

    def test_delete_key_at_end(self):
        l = LinkedList()
        l.insert_at_beginning(4)
        l.insert_at_beginning(9)
        l.insert_at_beginning(3)
        res = l.delete_key(4)
        assert res == 4
        assert l.count() == 2


