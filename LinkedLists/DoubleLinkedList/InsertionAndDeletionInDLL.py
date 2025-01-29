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

    def insert_before(self, target_value, value):
        """Insert a node before a given node."""
        if not self.head:
            print("List is empty.")
            return

        current = self.head
        while current and current.data != target_value:
            current = current.next

        if not current:
            print(f"Node with value {target_value} not found.")
            return

        new_node = Node(value)
        new_node.next = current
        new_node.prev = current.prev

        if current.prev:
            current.prev.next = new_node
        else:
            self.head = new_node  # Update head if inserting at beginning

        current.prev = new_node

    def insert_after(self, target_value, value):
        """Insert a node after a given node."""
        current = self.head
        while current and current.data != target_value:
            current = current.next

        if not current:
            print(f"Node with value {target_value} not found.")
            return

        new_node = Node(value)
        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def delete_before(self, target_value):
        """Delete the node before a given node."""
        if not self.head or not self.head.next:
            print("List is too short to delete before a node.")
            return

        current = self.head.next  # Start from second node
        while current and current.data != target_value:
            current = current.next

        if not current or not current.prev:
            print(f"No node exists before {target_value}.")
            return

        node_to_delete = current.prev
        if node_to_delete.prev:
            node_to_delete.prev.next = current
        else:
            self.head = current  # Update head if deleting first node

        current.prev = node_to_delete.prev
        del node_to_delete

    def delete_after(self, target_value):
        """Delete the node after a given node."""
        current = self.head
        while current and current.data != target_value:
            current = current.next

        if not current or not current.next:
            print(f"No node exists after {target_value}.")
            return

        node_to_delete = current.next
        current.next = node_to_delete.next

        if node_to_delete.next:
            node_to_delete.next.prev = current

        del node_to_delete


# Example Usage
if __name__ == "__main__":
    dll = DoublyLinkedList()

    # Insert nodes
    for value in [10, 20, 30, 40, 50]:
        dll.insert_at_end(value)

    print("Original Doubly Linked List:")
    dll.traverse_forward()

    # Insert before a node
    dll.insert_before(30, 25)
    print("\nAfter inserting 25 before 30:")
    dll.traverse_forward()

    # Insert after a node
    dll.insert_after(30, 35)
    print("\nAfter inserting 35 after 30:")
    dll.traverse_forward()

    # Delete before a node
    dll.delete_before(30)
    print("\nAfter deleting node before 30:")
    dll.traverse_forward()

    # Delete after a node
    dll.delete_after(30)
    print("\nAfter deleting node after 30:")
    dll.traverse_forward()
