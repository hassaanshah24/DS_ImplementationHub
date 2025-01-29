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

    def reverse_list(self):
        """Reverse the entire doubly linked list."""
        current = self.head
        prev_node = None

        while current:
            # Swap next and prev pointers
            next_node = current.next
            current.next = prev_node
            current.prev = next_node

            # Move prev_node and current forward
            prev_node = current
            current = next_node

        # Reset head to the last processed node
        if prev_node:
            self.head = prev_node

    def reverse_between_positions(self, start, end):
        """Reverse a portion of the list between two given positions."""
        if start >= end or not self.head:
            return

        # Step 1: Navigate to the start position
        current = self.head
        position = 0
        while current and position < start:
            current = current.next
            position += 1

        if not current:
            return  # Start position is out of range

        left_node = current.prev  # Node before the start of reversal
        sublist_tail = current

        # Step 2: Reverse sublist from start to end position
        prev_node = None
        while current and position <= end:
            next_node = current.next
            current.next = prev_node
            current.prev = next_node
            prev_node = current
            current = next_node
            position += 1

        # Step 3: Reconnect reversed portion
        if left_node:
            left_node.next = prev_node
        else:
            self.head = prev_node  # Update head if reversal starts from the first node

        if sublist_tail:
            sublist_tail.next = current
            if current:
                current.prev = sublist_tail


# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()

    # Insert nodes
    for value in [10, 20, 30, 40, 50, 60, 70]:
        dll.insert_at_end(value)

    print("Original Doubly Linked List:")
    dll.traverse_forward()

    # Reverse entire list
    dll.reverse_list()
    print("Reversed Doubly Linked List:")
    dll.traverse_forward()

    # Re-inserting to original order for partial reversal
    dll = DoublyLinkedList()
    for value in [10, 20, 30, 40, 50, 60, 70]:
        dll.insert_at_end(value)

    # Reverse a portion of the list (e.g., between position 2 and 5)
    dll.reverse_between_positions(2, 5)
    print("Doubly Linked List after reversing between positions 2 and 5:")
    dll.traverse_forward()
