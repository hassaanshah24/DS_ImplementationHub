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

def sort_linked_list_non_recursive(stack):
    """Sort the linked list without recursion."""
    helper_stack = LinkedListStack()
    while not stack.is_empty():
        temp = stack.pop()

        while not helper_stack.is_empty() and helper_stack.top.data > temp:
            stack.push(helper_stack.pop())

        helper_stack.push(temp)

    # Transfer back to the original stack
    while not helper_stack.is_empty():
        stack.push(helper_stack.pop())

def print_linked_list(stack):
    """Print the linked list."""
    current = stack.top
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

if __name__ == "__main__":
    stack = LinkedListStack()
    stack.push(30)
    stack.push(10)
    stack.push(50)
    stack.push(20)
    stack.push(40)

    print("Original Linked List Stack:")
    print_linked_list(stack)

    # Sort the stack without recursion
    sort_linked_list_non_recursive(stack)

    print("\nSorted Linked List Stack:")
    print_linked_list(stack)
