class Node:
    """A class representing a node in a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """A singly linked list with a tail pointer for efficient insertions."""

    def __init__(self):
        self.head = None
        self.tail = None  # Tail pointer for O(1) insertions at the end

    def insert_at_end(self, data):
        """Insert a new node at the end in O(1) time."""
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node  # Update tail pointer

    def find_middle(self):
        """Find the middle element using the slow-fast pointer (Tortoise & Hare) approach."""
        if self.head is None:
            return None

        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next  # Moves one step
            fast = fast.next.next  # Moves two steps

        return slow.data  # Middle element

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
    sll.insert_at_end(50)

    print("Original List:")
    sll.display()

    middle_value = sll.find_middle()
    print(f"Middle Element: {middle_value}")
