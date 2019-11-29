# Linked List with Tail Pointer
# Singly Linked

from src.linked_list.linked_list_node import LinkedListNode

class LinkedListWithTailPointer:

    def __init__(self):
        self.head = None
        self.tail = None


    def insert_at_end(self, data):
        n = LinkedListNode(data)
        if self.tail is None:
            self.tail = n
            self.head = n
        else:
            self.tail = n
            self.tail.next = n


    def is_empty(self):
        return self.head is None


    def count(self):
        if self.is_empty():
            return 0
        if self.head == self.tail:
            return 1
        n = self.head
        count = 0
        while n != self.tail:
            count += 1
            n = n.next
        return count
