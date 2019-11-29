from src.linked_list.linked_list_with_tail_pointer import LinkedListWithTailPointer

class TestLinkedListWithTailPointer:

    def test_insert_at_end(self):
        l = LinkedListWithTailPointer()
        l.insert_at_end(50)
        assert l.count() == 1