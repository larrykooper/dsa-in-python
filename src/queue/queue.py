""" queue

    I implement queue as a linked list with tail pointer
"""
from src.linked_list.linked_list_with_tail_pointer import LinkedListWithTailPointer

class Queue:

    def __init__(self):
        self.list = LinkedListWithTailPointer()

    # Enqueue means add at end
    def enqueue(self, data):
        self.list.insert_at_end(data)

    # Dequeue means remove at beginning
    def dequeue(self):
        return self.list.remove_from_beginning()

    def count(self):
        return self.list.count()






