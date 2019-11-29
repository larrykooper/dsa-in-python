"""
I will implement stack as a linked list
"""
from linked_list import LinkedList

class Stack:

    def __init__(self):
        self.list = LinkedList()

    def push(self, data):
        self.list.insert_at_beginning(data)
        return self

    def pop(self):
        return self.list.remove_from_beginning()

    def count(self):
        return self.list.count()