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

    def split_in_half(self):
        """Split the linked list into two halves."""
        if not self.head or not self.head.next:
            return None, None  # Empty or single node list cannot be split
        slow = self.head
        fast = self.head
        prev = None
        # Move fast pointer by 2 steps and slow pointer by 1 step
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        # Split the list into two halves
        prev.next = None

        # Create two new lists for the two halves
        first_half = SinglyLinkedList()
        second_half = SinglyLinkedList()

        first_half.head = self.head
        second_half.head = slow

        return first_half, second_half

    def split_even_odd(self):
        """Split the linked list into even and odd indexed nodes."""
        even_list = SinglyLinkedList()
        odd_list = SinglyLinkedList()
        current = self.head
        index = 0
        while current:
            if index % 2 == 0:
                even_list.insert_at_end(current.data)
            else:
                odd_list.insert_at_end(current.data)
            current = current.next
            index += 1
        return even_list, odd_list

    def partition_around_value(self, value):
        """Partition the linked list around a value."""
        smaller = SinglyLinkedList()
        greater_or_equal = SinglyLinkedList()
        current = self.head
        while current:
            if current.data < value:
                smaller.insert_at_end(current.data)
            else:
                greater_or_equal.insert_at_end(current.data)
            current = current.next
        # Combine smaller and greater_or_equal lists
        if smaller.head:
            smaller_last = smaller.head
            while smaller_last.next:
                smaller_last = smaller_last.next
            smaller_last.next = greater_or_equal.head
            return smaller
        else:
            return greater_or_equal

# Example usage
if __name__ == "__main__":
    list1 = SinglyLinkedList()
    list1.insert_at_end(10)
    list1.insert_at_end(20)
    list1.insert_at_end(30)
    list1.insert_at_end(40)
    list1.insert_at_end(50)
    list1.insert_at_end(60)

    print("Original List:")
    list1.traverse()

    # Split the list into two halves
    first_half, second_half = list1.split_in_half()
    print("First Half:")
    first_half.traverse()
    print("Second Half:")
    second_half.traverse()

    # Split the list into even and odd indexed nodes
    even_list, odd_list = list1.split_even_odd()
    print("Even Indexed List:")
    even_list.traverse()
    print("Odd Indexed List:")
    odd_list.traverse()

    # Partition the list around a value (e.g., 35)
    partitioned_list = list1.partition_around_value(35)
    print("Partitioned List around 35:")
    partitioned_list.traverse()
