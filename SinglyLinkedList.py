class Node:
    def __init__(self, data):
        self.data = data  # Initialize node's data
        self.next = None  # Initialize next as null


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # End of list indicator

    def append_at_end(self, key):
        new_node = Node(key)

        if self.head is None:
            self.head = new_node

        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def append_at_start(self, key):
        new_node = Node(key)

        new_node.next = self.head
        self.head = new_node

    def delete_at_beginning(self):
        # Case: List is empty
        if self.head is None:
            print("The list is empty. No nodes to delete.")
            return
        # Move head to the next node
        self.head = self.head.next

    def delete_at_end(self):
        # Case: List is empty
        if self.head is None:
            print("The list is empty. No nodes to delete.")
            return
        # Case: Only one node in the list
        if self.head.next is None:
            self.head = None
            return
        # Traverse to the second-to-last node
        current = self.head
        while current.next.next:
            current = current.next
        # Unlink the last node
        current.next = None

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            self.append_at_start(data)
            return

        current = self.head
        current_position = 0

        # Traverse to the node just before the desired position
        while current is not None and current_position < position - 1:
            current = current.next
            current_position += 1

        if current is None:
            print("Position out of bounds.")
            return

        # Insert the new node by adjusting pointers
        new_node.next = current.next
        current.next = new_node

    def delete_at_position(self, position):
        # Case: List is empty
        if self.head is None:
            print("The list is empty. No nodes to delete.")
            return

        # Case: Delete the first node
        if position == 0:
            self.head = self.head.next
            return

        current = self.head
        current_position = 0

        # Traverse to the node just before the desired position
        while current.next is not None and current_position < position - 1:
            current = current.next
            current_position += 1

        if current.next is None:
            print("Position out of bounds.")
            return

        # Unlink the node at the specified position
        current.next = current.next.next


ll = LinkedList()
elements = [3, 5, 7, 10, 15]  # Elements to add to the linked list

for elem in elements:
    ll.append_at_end(elem)

print("Linked list elements:")
ll.display()


# Insert at specific positions
ll.insert_at_position(1, 0)  # Insert 1 at position 0 (beginning)
print("Linked list after inserting 1 at position 0:")
ll.display()

ll.insert_at_position(8, 3)  # Insert 8 at position 3
print("Linked list after inserting 8 at position 3:")
ll.display()

# Delete at specific positions
ll.delete_at_position(0)  # Delete at position 0 (beginning)
print("Linked list after deleting node at position 0:")
ll.display()

ll.delete_at_position(3)  # Delete at position 3
print("Linked list after deleting node at position 3:")
ll.display()

ll2 = LinkedList()

for elem in elements:
    ll2.append_at_start(elem)

print("Linked list elements:")
ll2.display()

# Delete at the beginning
ll.delete_at_beginning()
print("After deleting at the beginning:")
ll.display()

# Delete at the end
ll2.delete_at_end()
print("After deleting at the end:")
ll2.display()
