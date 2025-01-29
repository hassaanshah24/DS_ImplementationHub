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
            print(f"Inserted {value} at the end.")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Inserted {value} at the end.")

    def search_by_value(self, value):
        """Search for a node with a specific value."""
        current = self.head
        index = 1
        while current:
            if current.data == value:
                print(f"Node with value {value} found at position {index}.")
                return
            current = current.next
            index += 1
        print(f"Node with value {value} not found.")

    def find_nth_from_beginning(self, n):
        """Find the nth node from the beginning."""
        current = self.head
        count = 1
        while current:
            if count == n:
                print(f"The {n}th node from the beginning is {current.data}.")
                return
            current = current.next
            count += 1
        print(f"The list has less than {n} nodes.")

    def find_nth_from_end(self, n):
        """Find the nth node from the end."""
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        if n > length:
            print(f"The list has less than {n} nodes.")
            return
        current = self.head
        for i in range(length - n):
            current = current.next
        print(f"The {n}th node from the end is {current.data}.")

    def find_middle_node(self):
        """Find the middle node of the linked list."""
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if slow:
            print(f"The middle node is {slow.data}.")
        else:
            print("The list is empty.")


# Example usage
if __name__ == "__main__":
    linked_list = SinglyLinkedList()

    # Insert nodes at the end
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)
    linked_list.insert_at_end(50)

    # Traverse and display all elements
    linked_list.traverse()

    # Search for a node by value
    linked_list.search_by_value(30)
    linked_list.search_by_value(100)

    # Find the nth node from the beginning
    linked_list.find_nth_from_beginning(3)
    linked_list.find_nth_from_beginning(6)

    # Find the nth node from the end
    linked_list.find_nth_from_end(2)
    linked_list.find_nth_from_end(6)

    # Find the middle node
    linked_list.find_middle_node()
