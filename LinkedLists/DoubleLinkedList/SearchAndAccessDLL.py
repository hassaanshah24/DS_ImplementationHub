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

    def search(self, value):
        """Search for a node with a specific value."""
        current = self.head
        position = 0
        while current:
            if current.data == value:
                print(f"Value {value} found at position {position}.")
                return
            current = current.next
            position += 1
        print(f"Value {value} not found in the list.")

    def find_nth_from_beginning(self, n):
        """Find the nth node from the beginning."""
        current = self.head
        position = 0
        while current:
            if position == n:
                print(f"The {n}th node from the beginning has the value: {current.data}")
                return
            current = current.next
            position += 1
        print(f"Position {n} is out of range.")

    def find_nth_from_end(self, n):
        """Find the nth node from the end."""
        # Step 1: Calculate the length of the list
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next

        # Step 2: Find the corresponding position from the beginning
        target = length - n - 1
        if target < 0:
            print(f"Position {n} from the end is out of range.")
            return

        # Step 3: Traverse to the target position
        current = self.head
        position = 0
        while current:
            if position == target:
                print(f"The {n}th node from the end has the value: {current.data}")
                return
            current = current.next
            position += 1
        print(f"Position {n} from the end is out of range.")


# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()

    # Insert nodes
    for value in [10, 20, 30, 40, 50]:
        dll.insert_at_end(value)

    print("Doubly Linked List:")
    dll.traverse_forward()

    # Search for a specific value
    dll.search(30)
    dll.search(60)

    # Find nth node from beginning
    dll.find_nth_from_beginning(2)
    dll.find_nth_from_beginning(5)

    # Find nth node from end
    dll.find_nth_from_end(1)
    dll.find_nth_from_end(4)
    dll.find_nth_from_end(6)
