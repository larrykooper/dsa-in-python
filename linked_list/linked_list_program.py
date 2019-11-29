from linked_list import LinkedList

l = LinkedList()

l.insert_at_beginning(6)
l.insert_at_beginning(3)
print(l)

myval = l.remove_from_beginning()
print("list:")
print(l)
print("value gotten")
print(myval)