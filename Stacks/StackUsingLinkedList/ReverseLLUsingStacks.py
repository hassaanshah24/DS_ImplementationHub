class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, value):
        """Push an element onto the stack."""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Pop an element from the stack."""
        if self.top is None:
            print("Stack is empty!")
            return None
        value = self.top.data
        self.top = self.top.next
        return value

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

    def display(self):
        """Display the stack contents."""
        current = self.top
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


def reverse_linked_list(linked_list):
    """Reverse the linked list using a stack."""
    stack = LinkedListStack()
    current = linked_list.top
    while current:
        stack.push(current.data)
        current = current.next

    # Pop elements from stack and reassign them to the linked list
    reversed_list = LinkedListStack()
    while not stack.is_empty():
        reversed_list.push(stack.pop())

    return reversed_list


if __name__ == "__main__":
    # Create a linked list
    linked_list = LinkedListStack()
    linked_list.push(10)
    linked_list.push(20)
    linked_list.push(30)
    linked_list.push(40)
    linked_list.push(50)

    print("Original Linked List:")
    linked_list.display()

    # Reverse the linked list
    reversed_linked_list = reverse_linked_list(linked_list)

    print("Reversed Linked List:")
    reversed_linked_list.display()
