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

    def swap_pairs(self):
        """Swap adjacent nodes in pairs."""
        if not self.head or not self.head.next:
            return  # No need to swap if less than 2 nodes

        prev = None
        curr = self.head

        # Swap the first pair of nodes
        self.head = curr.next  # The second node becomes the head
        while curr and curr.next:
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = curr
            if prev:
                prev.next = next_node  # Connect the previous node to the swapped pair
            prev = curr
            curr = curr.next  # Move to the next pair

        # Update the tail if the list has an odd number of nodes
        if curr:
            self.tail = curr

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
    sll.insert_at_end(1)
    sll.insert_at_end(2)
    sll.insert_at_end(3)
    sll.insert_at_end(4)
    sll.insert_at_end(5)

    print("Original List:")
    sll.display()

    sll.swap_pairs()
    print("After Swapping Pairs:")
    sll.display()