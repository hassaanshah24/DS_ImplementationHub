class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        """Insert a node at the end of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def traverse_forward(self):
        """Traverse and display all elements from head (forward traversal)."""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def count_nodes(self):
        """Count the total number of nodes in the doubly linked list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None

# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()

    # Check if the list is empty
    print("Is the list empty?", dll.is_empty())  # Output: True

    # Insert nodes
    for value in [10, 20, 30, 40, 50]:
        dll.insert_at_end(value)

    print("Doubly Linked List:")
    dll.traverse_forward()

    # Count total nodes
    print("Total number of nodes:", dll.count_nodes())  # Output: 5

    # Check if the list is empty after inserting elements
    print("Is the list empty?", dll.is_empty())  # Output: False
