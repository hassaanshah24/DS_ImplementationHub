class Node:
    def __init__(self, value):
        self.data = value  # Store the value of the node
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list

    def insert_at_end(self, value):
        new_node = Node(value)  # Create a new node
        if not self.head:  # If the list is empty, set head to new node
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node  # Link last node to the new node
        new_node.prev = current  # Set previous pointer of new node

    def traverse_forward(self):
        current = self.head
        while current:  # Traverse the list forward
            print(current.data, end=" <-> ")
            current = current.next
        print("None")  # Indicate end of the list

    def bubble_sort(self):
        if not self.head:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.data > current.next.data:  # Swap if out of order
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return

        current = self.head.next
        while current:
            key = current.data
            temp = current.prev

            while temp and temp.data > key:  # Shift larger elements forward
                temp.next.data = temp.data
                temp = temp.prev

            if temp:
                temp.next.data = key  # Insert element at correct position
            else:
                self.head.data = key  # Update head if necessary

            current = current.next

    def merge_sort(self):
        if not self.head or not self.head.next:
            return
        self.head = self._merge_sort(self.head)  # Recursively sort list

    def _merge_sort(self, head):
        if not head or not head.next:
            return head

        middle = self._get_middle(head)  # Get middle of the list
        next_to_middle = middle.next
        middle.next = None  # Split the list into two halves

        left = self._merge_sort(head)  # Recursively sort first half
        right = self._merge_sort(next_to_middle)  # Recursively sort second half

        return self._sorted_merge(left, right)  # Merge the two sorted halves

    def _get_middle(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:  # Move fast pointer twice as fast as slow
            slow = slow.next
            fast = fast.next.next
        return slow  # Slow will be at the middle

    def _sorted_merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.data <= right.data:
            result = left
            result.next = self._sorted_merge(left.next, right)  # Merge remaining nodes
            if result.next:
                result.next.prev = result  # Maintain previous pointer
        else:
            result = right
            result.next = self._sorted_merge(left, right.next)
            if result.next:
                result.next.prev = result

        return result


if __name__ == "__main__":
    dll = DoublyLinkedList()
    for value in [50, 20, 40, 10, 30]:
        dll.insert_at_end(value)

    print("Original Doubly Linked List:")
    dll.traverse_forward()

    dll.bubble_sort()
    print("\nSorted List (Bubble Sort):")
    dll.traverse_forward()

    dll = DoublyLinkedList()
    for value in [50, 20, 40, 80, 30]:
        dll.insert_at_end(value)

    dll.insertion_sort()
    print("\nSorted List (Insertion Sort):")
    dll.traverse_forward()

    dll = DoublyLinkedList()
    for value in [60, 20, 40, 10, 30]:
        dll.insert_at_end(value)

    dll.merge_sort()
    print("\nSorted List (Merge Sort):")
    dll.traverse_forward()
