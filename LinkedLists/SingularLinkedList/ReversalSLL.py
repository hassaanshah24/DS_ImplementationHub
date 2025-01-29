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

    def reverse_entire(self):
        """Reverse the entire linked list."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        print("The list has been reversed.")

    def reverse_between(self, m, n):
        """Reverse a portion of the linked list between positions m and n."""
        if m == n:
            return

        # Initialize dummy node and set up pointers
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        for _ in range(m - 1):
            prev = prev.next
        current = prev.next
        next_node = current.next

        # Reverse the portion between m and n
        for _ in range(n - m):
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
            next_node = current.next

        self.head = dummy.next
        print(f"Reversed the portion between positions {m} and {n}.")

    def reverse_in_groups(self, k):
        """Reverse nodes in groups of k."""
        if not self.head or k == 1:
            return

        # Helper function to reverse a linked list of size k
        def reverse_k_nodes(head, k):
            prev, current = None, head
            count = 0
            while current and count < k:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                count += 1
            return prev

        # Dummy node to handle edge cases
        dummy = Node(0)
        dummy.next = self.head
        group_prev = dummy
        while True:
            kth_node = group_prev
            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    return
            group_next = kth_node.next
            group_start = group_prev.next
            group_prev.next = reverse_k_nodes(group_start, k)
            group_start.next = group_next
            group_prev = group_start

        print(f"Reversed the list in groups of {k}.")


# Example usage
if __name__ == "__main__":
    linked_list = SinglyLinkedList()

    # Insert nodes at the end
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)
    linked_list.insert_at_end(50)
    linked_list.insert_at_end(60)

    print("Original List:")
    linked_list.traverse()

    # Reverse the entire list
    linked_list.reverse_entire()
    linked_list.traverse()

    # Reverse a portion of the list (between positions 2 and 5)
    linked_list.reverse_between(2, 5)
    linked_list.traverse()

    # Reverse in groups of 3
    linked_list.reverse_in_groups(3)
    linked_list.traverse()
