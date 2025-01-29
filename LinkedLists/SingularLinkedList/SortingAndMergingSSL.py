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

    def merge_sort(self, head):
        """Sort the linked list using Merge Sort."""
        if not head or not head.next:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        return self.merge(left, right)

    def get_middle(self, head):
        """Find the middle node of the linked list."""
        if not head:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        """Merge two sorted linked lists into one sorted list."""
        if not left:
            return right
        if not right:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)
        return result

    def insertion_sort(self):
        """Sort the linked list using Insertion Sort."""
        if not self.head or not self.head.next:
            return self.head

        sorted_list = None
        current = self.head

        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node

        self.head = sorted_list
        return self.head

    def sorted_insert(self, sorted_list, new_node):
        """Helper function to insert a node in the sorted linked list."""
        if not sorted_list or new_node.data <= sorted_list.data:
            new_node.next = sorted_list
            sorted_list = new_node
        else:
            current = sorted_list
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        return sorted_list

    def merge_sorted_lists(self, list2):
        """Merge two sorted linked lists into one sorted linked list."""
        merged_list = SinglyLinkedList()
        current1 = self.head
        current2 = list2.head

        while current1 and current2:
            if current1.data <= current2.data:
                merged_list.insert_at_end(current1.data)
                current1 = current1.next
            else:
                merged_list.insert_at_end(current2.data)
                current2 = current2.next

        while current1:
            merged_list.insert_at_end(current1.data)
            current1 = current1.next

        while current2:
            merged_list.insert_at_end(current2.data)
            current2 = current2.next

        return merged_list

    def concatenate_lists(self, list2):
        """Concatenate two linked lists."""
        if not self.head:
            self.head = list2.head
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = list2.head


# Example usage
if __name__ == "__main__":
    list1 = SinglyLinkedList()
    list1.insert_at_end(30)
    list1.insert_at_end(10)
    list1.insert_at_end(20)
    list1.insert_at_end(50)
    list1.insert_at_end(40)

    print("Original list:")
    list1.traverse()

    # Merge Sort
    sorted_list = SinglyLinkedList()
    sorted_list.head = list1.merge_sort(list1.head)
    print("Sorted list using Merge Sort:")
    sorted_list.traverse()

    # Insertion Sort
    list1.insertion_sort()
    print("Sorted list using Insertion Sort:")
    list1.traverse()

    # Merging two sorted lists
    list2 = SinglyLinkedList()
    list2.insert_at_end(5)
    list2.insert_at_end(15)
    list2.insert_at_end(25)

    print("List 2:")
    list2.traverse()

    merged_list = list1.merge_sorted_lists(list2)
    print("Merged sorted list:")
    merged_list.traverse()

    # Concatenate two lists
    list1.concatenate_lists(list2)
    print("Concatenated list:")
    list1.traverse()
