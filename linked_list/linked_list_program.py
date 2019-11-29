from linked_list import LinkedList

l = LinkedList()

l.insert_at_beginning(6)
l.insert_at_beginning(3)
print(l.display_recursive('\n'))

myval = l.remove_from_beginning()
print("list:")
print(l.display_recursive('\n'))

print("value gotten")
print(myval)