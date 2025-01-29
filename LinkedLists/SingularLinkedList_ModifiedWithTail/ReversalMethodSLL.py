class Node:
    """A class representing a node in a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """Singly Linked List with Tail Pointer for efficient operations."""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        """Insert a new node at the end in O(1) time."""
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def reverse_in_groups(self, k):
        """Reverse nodes in groups of size k."""
        current = self.head
        prev_tail = None
        new_head = None

        while current:
            count = 0
            current_group_head = current
            prev = None
            while current and count < k:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                count += 1

            if not new_head:
                new_head = prev

            if prev_tail:
                prev_tail.next = prev

            prev_tail = current_group_head

        self.head = new_head

    def display(self):
        """Display the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_end(1)
    sll.insert_at_end(2)
    sll.insert_at_end(3)
    sll.insert_at_end(4)
    sll.insert_at_end(5)
    sll.insert_at_end(6)

    print("Original List:")
    sll.display()

    sll.reverse_in_groups(3)
    print("After Reversing in Groups of 3:")
    sll.display()
