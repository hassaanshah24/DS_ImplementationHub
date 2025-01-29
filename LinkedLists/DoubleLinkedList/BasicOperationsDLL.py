class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def traverse_forward(self):
        """Traverse and display all elements from head (forward traversal)."""
        current = self.head
        if not current:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        """Traverse and display all elements from tail (backward traversal)."""
        current = self.head
        if not current:
            print("The list is empty.")
            return
        # Traverse to the last node
        while current.next:
            current = current.next
        # Now traverse backward
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

    def insert_at_beginning(self, value):
        """Insert a node at the beginning of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

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

    def insert_at_position(self, value, position):
        """Insert a node at a specific position."""
        new_node = Node(value)
        if position == 0:  # Insert at the beginning
            self.insert_at_beginning(value)
            return
        current = self.head
        count = 0
        while current:
            if count == position - 1:
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                new_node.prev = current
                return
            count += 1
            current = current.next
        print("Position out of range!")

    def delete_from_beginning(self):
        """Delete a node from the beginning of the list."""
        if not self.head:
            print("The list is empty.")
            return
        if not self.head.next:  # Only one node
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_from_end(self):
        """Delete a node from the end of the list."""
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        while current.next:
            current = current.next
        if current.prev:  # If more than one node
            current.prev.next = None
        else:  # Only one node
            self.head = None

    def delete_at_position(self, position):
        """Delete a node at a specific position."""
        if not self.head:
            print("The list is empty.")
            return
        if position == 0:  # Delete from the beginning
            self.delete_from_beginning()
            return
        current = self.head
        count = 0
        while current:
            if count == position:
                if current.next:
                    current.next.prev = current.prev
                if current.prev:
                    current.prev.next = current.next
                current = None
                return
            count += 1
            current = current.next
        print("Position out of range!")

    def delete_by_value(self, value):
        """Delete a node by its value."""
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  # If it's the first node
                    self.head = current.next
                current = None
                return
            current = current.next
        print(f"Node with value {value} not found!")


# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()

    # Insert nodes
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_beginning(5)

    print("List after insertions:")
    dll.traverse_forward()  # Forward traversal

    # Insert at specific position
    dll.insert_at_position(25, 2)
    print("List after inserting 25 at position 2:")
    dll.traverse_forward()

    # Delete nodes
    dll.delete_from_beginning()
    print("List after deleting from the beginning:")
    dll.traverse_forward()

    dll.delete_from_end()
    print("List after deleting from the end:")
    dll.traverse_forward()

    dll.delete_at_position(1)
    print("List after deleting node at position 1:")
    dll.traverse_forward()

    # Delete by value
    dll.delete_by_value(20)
    print("List after deleting node with value 20:")
    dll.traverse_forward()

    # Backward traversal
    print("Backward traversal:")
    dll.traverse_backward()
