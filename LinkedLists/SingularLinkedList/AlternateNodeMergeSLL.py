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

    def alternate_merge(self, list2):
        """Alternate merge two linked lists."""
        list1_current = self.head
        list2_current = list2.head
        # Create a dummy node to simplify the merge process
        dummy = Node(0)
        current = dummy
        while list1_current and list2_current:
            # Add node from list1
            current.next = list1_current
            list1_current = list1_current.next
            current = current.next
            # Add node from list2
            current.next = list2_current
            list2_current = list2_current.next
            current = current.next
        # If there are remaining nodes in list1
        if list1_current:
            current.next = list1_current
        # If there are remaining nodes in list2
        if list2_current:
            current.next = list2_current
        # Set the merged list's head
        self.head = dummy.next

# Example usage
if __name__ == "__main__":
    list1 = SinglyLinkedList()
    list1.insert_at_end(1)
    list1.insert_at_end(3)
    list1.insert_at_end(5)
    list1.insert_at_end(7)

    list2 = SinglyLinkedList()
    list2.insert_at_end(2)
    list2.insert_at_end(4)
    list2.insert_at_end(6)

    print("List 1:")
    list1.traverse()

    print("List 2:")
    list2.traverse()

    # Alternate merge the two lists
    list1.alternate_merge(list2)

    print("Alternately Merged List:")
    list1.traverse()
