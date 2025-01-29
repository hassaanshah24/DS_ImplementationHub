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

    def swap_nodes(self, value1, value2):
        """Swap two nodes without swapping their data."""
        if value1 == value2:
            print("Both nodes are the same, no swap needed.")
            return

        node1 = node2 = None
        current = self.head

        # Find nodes with the given values
        while current:
            if current.data == value1:
                node1 = current
            elif current.data == value2:
                node2 = current
            current = current.next

        if not node1 or not node2:
            print("One or both values not found in the list.")
            return

        # Swap previous pointers
        if node1.prev:
            node1.prev.next = node2
        else:  # If node1 is head, update head
            self.head = node2

        if node2.prev:
            node2.prev.next = node1
        else:  # If node2 is head, update head
            self.head = node1

        # Swap next pointers
        if node1.next:
            node1.next.prev = node2
        if node2.next:
            node2.next.prev = node1

        # Swap node1 and node2 pointers
        node1.prev, node2.prev = node2.prev, node1.prev
        node1.next, node2.next = node2.next, node1.next

    def swap_adjacent_nodes(self, value1, value2):
        """Handles case when nodes are adjacent to each other."""
        if value1 == value2:
            print("Both nodes are the same, no swap needed.")
            return

        node1 = node2 = None
        current = self.head

        # Find nodes with the given values
        while current:
            if current.data == value1:
                node1 = current
            elif current.data == value2:
                node2 = current
            current = current.next

        if not node1 or not node2:
            print("One or both values not found in the list.")
            return

        # Ensure node1 comes before node2 in the list
        if node1.next != node2:
            node1, node2 = node2, node1

        # Update previous pointers
        if node1.prev:
            node1.prev.next = node2
        else:
            self.head = node2

        if node2.next:
            node2.next.prev = node1

        # Swap adjacent nodes
        node1.next, node2.next = node2.next, node1
        node2.prev, node1.prev = node1.prev, node2


# Example Usage
if __name__ == "__main__":
    dll = DoublyLinkedList()

    # Insert nodes
    for value in [10, 20, 30, 40, 50]:
        dll.insert_at_end(value)

    print("Original Doubly Linked List:")
    dll.traverse_forward()

    # Swap non-adjacent nodes
    dll.swap_nodes(20, 50)
    print("\nAfter swapping 20 and 50:")
    dll.traverse_forward()

    # Swap adjacent nodes
    dll.swap_adjacent_nodes(30, 40)
    print("\nAfter swapping adjacent nodes 30 and 40:")
    dll.traverse_forward()
