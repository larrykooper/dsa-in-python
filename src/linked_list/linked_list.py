from src.linked_list.linked_list_node import LinkedListNode

# THIS IS A SINGLY LINKED LIST

class LinkedList:

    def __init__(self):
        # head is a LinkedListNode
        self.head = None

    # pass delim = '\n' to display on separate lines
    def display_iterative(self, delim):
        retval = ''
        n = self.head
        while n.next is not None:
            retval += str(n.data) + delim
            n = n.next
        retval += str(n.data)
        return retval


    def display_recursive(self, delim):
        if self.is_empty():
            return ''
        retval = ''
        n = self.head
        retval += str(n.data) + delim
        l = LinkedList()
        l.head = n.next
        retval += l.display_recursive(delim)
        return retval


    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        n = LinkedListNode(data)
        n.next = self.head
        self.head = n
        return self

    # If list is empty, return None
    def remove_from_beginning(self):
        if self.is_empty():
            return None
        retval = self.head.data
        self.head = self.head.next
        return retval

    # deletes first appearance of key
    # return None if not found, key if found
    def delete_key(self, key):
        lead_pointer = self.head
        trail_pointer = self.head
        while lead_pointer.next is not None:
            if lead_pointer.data == key:
                self.remove_key_and_adjust(lead_pointer, trail_pointer)
                return key
            trail_pointer = lead_pointer
            lead_pointer = lead_pointer.next
        # If here, lead_pointer points to last element
        if lead_pointer.data == key:
            self.remove_key_and_adjust(lead_pointer, trail_pointer)
            return key
        else:
            return None


    def remove_key_and_adjust(self, lead_pointer, trail_pointer):
        if trail_pointer == lead_pointer:
            self.head = self.head.next
        else:
            trail_pointer.next = lead_pointer.next

    def count(self):
        if self.is_empty():
            return 0
        n = self.head
        count = 0
        while n.next is not None:
            count += 1
            n = n.next
        count += 1
        return count

    # returns query if found, returns None if not
    def search(self, query):
        n = self.head
        while n.next is not None:
            if n.data == query:
                return query
            n = n.next
        if n.data == query:
            return query
        else:
            return None



