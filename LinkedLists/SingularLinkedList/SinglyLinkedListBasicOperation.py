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

    def insert_at_beginning(self, value):
        """Insert a node at the beginning of the list."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {value} at the beginning.")

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

    def insert_at_position(self, value, position):
        """Insert a node at a specific position."""
        new_node = Node(value)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            print(f"Inserted {value} at position {position}.")
            return
        current = self.head
        count = 1
        while current and count < position - 1:
            current = current.next
            count += 1
        if not current:
            print("Position out of range.")
            return
        new_node.next = current.next
        current.next = new_node
        print(f"Inserted {value} at position {position}.")

    def delete_by_value(self, value):
        """Delete the first node with the specified value."""
        current = self.head
        if not current:
            print("The list is empty.")
            return
        if current.data == value:
            self.head = current.next
            print(f"Deleted {value} from the list.")
            return
        prev = None
        while current and current.data != value:
            prev = current
            current = current.next
        if not current:
            print(f"Value {value} not found in the list.")
            return
        prev.next = current.next
        print(f"Deleted {value} from the list.")

    def delete_at_position(self, position):
        """Delete the node at a specific position."""
        if position == 1:
            if self.head:
                self.head = self.head.next
                print(f"Deleted node at position {position}.")
            else:
                print("The list is empty.")
            return
        current = self.head
        count = 1
        prev = None
        while current and count < position:
            prev = current
            current = current.next
            count += 1
        if not current:
            print("Position out of range.")
            return
        prev.next = current.next
        print(f"Deleted node at position {position}.")

    def delete_from_beginning(self):
        """Delete the node from the beginning."""
        if self.head:
            self.head = self.head.next
            print("Deleted node from the beginning.")
        else:
            print("The list is empty.")

    def delete_from_end(self):
        """Delete the node from the end."""
        if not self.head:
            print("The list is empty.")
            return
        if not self.head.next:
            self.head = None
            print("Deleted node from the end.")
            return
        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None
        print("Deleted node from the end.")


# Example usage
if __name__ == "__main__":
    linked_list = SinglyLinkedList()

    # Insert nodes at the beginning
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(20)
    linked_list.insert_at_beginning(30)

    # Insert nodes at the end
    linked_list.insert_at_end(40)
    linked_list.insert_at_end(50)

    # Insert node at specific position
    linked_list.insert_at_position(25, 3)

    # Traverse and display all elements
    linked_list.traverse()

    # Delete node by value
    linked_list.delete_by_value(20)
    linked_list.traverse()

    # Delete node at specific position
    linked_list.delete_at_position(2)
    linked_list.traverse()

    # Delete node from the beginning
    linked_list.delete_from_beginning()
    linked_list.traverse()

    # Delete node from the end
    linked_list.delete_from_end()
    linked_list.traverse()
