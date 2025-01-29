class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        """Traverse and display all elements in the linked list."""
        current = self.head
        if not current:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

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

    def count_nodes(self):
        """Count the total number of nodes in the linked list."""
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        """Check if the linked list is empty."""
        return self.head is None

# Example usage
if __name__ == "__main__":
    linked_list = SinglyLinkedList()

    # Insert nodes at the end
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)
    linked_list.insert_at_end(50)

    # Traverse and display the list
    print("Linked List:")
    linked_list.traverse()

    # Count total number of nodes
    print("Total number of nodes:", linked_list.count_nodes())

    # Check if the linked list is empty
    print("Is the list empty?", "Yes" if linked_list.is_empty() else "No")

    # Remove all nodes and check again
    linked_list.head = None
    print("After clearing the list:")
    print("Total number of nodes:", linked_list.count_nodes())
    print("Is the list empty?", "Yes" if linked_list.is_empty() else "No")
