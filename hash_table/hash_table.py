""" I will implement HashTable as an array (a list, in Pascal-speak) of linked lists.

    size of hash table will be 23.
    Hash function will be h(k) = k mod 23
    23 is a prime not too close to a power of 2
    We don't want a power of 2 because then not all the bits of k will determine h(k)
"""

from linked_list import LinkedList

class HashTable:


    def __init__(self):
        self.table_size = 23
        self.array = [None] * self.table_size

    def insert(self, key):
        slot = self.h(key)
        if self.array[slot] is None:
            l = LinkedList()
            self.array[slot] = l
        self.array[slot].insert_at_beginning(key)
        return self

    # search for an element with key = key
    def search(self, key):
        slot = self.h(key)   # LKHERE

    # hash function
    def h(self, key):
        return key % self.table_size

    def slot_cardinality(self, slot):
        return self.array[slot].count()



