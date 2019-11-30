from src.linked_list.linked_list_with_tail_pointer import LinkedListWithTailPointer

class TestLinkedListWithTailPointer:

    def test_insert_at_end_if_zero(self):
        l = LinkedListWithTailPointer()
        l.insert_at_end(50)
        assert l.count() == 1

    def test_remove_from_beginning_if_1(self):
        l = LinkedListWithTailPointer()
        l.insert_at_end(50)
        retval = l.remove_from_beginning()
        assert l.is_empty()
        assert retval == 50

    def test_insert_at_end_if_1(self):
        l = LinkedListWithTailPointer()
        l.insert_at_end(8)
        l.insert_at_end(16)
        assert l.count() == 2


    def test_insert_at_end_if_3(self):
        l = LinkedListWithTailPointer()
        l.insert_at_end(3)
        l.insert_at_end(6)
        l.insert_at_end(19)
        l.insert_at_end(10)
        assert l.count() == 4