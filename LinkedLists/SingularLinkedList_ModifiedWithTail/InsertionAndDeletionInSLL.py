class Node:
    """A class representing a node in a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """A singly linked list with a tail pointer for efficient insertions at the end."""

    def __init__(self):
        self.head = None
        self.tail = None  # Tail pointer for O(1) insertion at the end

    def insert_at_end(self, data):
        """Insert a new node at the end in O(1) time."""
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node  # Update tail pointer

    def delete_from_end(self):
        """Delete the last node and update the tail pointer."""
        if self.head is None:
            print("List is empty, nothing to delete.")
            return

        if self.head == self.tail:  # If only one node exists
            self.head = self.tail = None
            return

        # Find the second last node
        current = self.head
        while current.next != self.tail:
            current = current.next

        current.next = None  # Remove last node
        self.tail = current  # Update tail pointer

    def display(self):
        """Display the linked list elements."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example Usage
if __name__ == "__main__":
   sll = SinglyLinkedList()
   sll.insert_at_end(10)
   sll.insert_at_end(20)
   sll.insert_at_end(30)
   sll.insert_at_end(40)

print("Original List:")
sll.display()

sll.delete_from_end()
print("After Deleting Last Node:")
sll.display()

sll.delete_from_end()
print("After Another Deletion:")
sll.display()
