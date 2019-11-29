from linked_list_node import LinkedListNode

class LinkedList:

    def __init__(self):
        # head is a LinkedListNode
        self.head = None

    def __str__(self):
        retval = ''
        n = self.head
        while n.next is not None:
            retval += str(n.data) + '\n'
            n = n.next
        retval += str(n.data)
        return retval


    def insert_at_beginning(self, data):
        n = LinkedListNode(data)
        n.next = self.head
        self.head = n
        return self


    def remove_from_beginning(self):
        retval = self.head.data
        self.head = self.head.next
        return retval

    def count(self):
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



