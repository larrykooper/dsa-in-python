from src.linked_list.linked_list_with_tail_pointer import LinkedListWithTailPointer

class TestLinkedListWithTailPointer:

    def test_insert_at_end(self):
        l = LinkedListWithTailPointer()
        l.insert_at_end(50)
        assert l.count() == 1

    def test_remove_from_beginning_if_1(self):
        l = LinkedListWithTailPointer()
        l.insert_at_end(50)
        retval = l.remove_from_beginning()
        assert l.is_empty()
        assert retval == 50

