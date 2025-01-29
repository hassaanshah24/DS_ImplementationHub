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
        print(f"Pushed {value} onto linked list stack.")

    def pop(self):
        """Pop an element from the stack."""
        if self.top is None:
            print("Stack is empty!")
            return None
        value = self.top.data
        self.top = self.top.next
        print(f"Popped {value} from linked list stack.")
        return value

    def peek(self):
        """View the top element of the stack."""
        if self.top is None:
            print("Stack is empty!")
            return None
        return self.top.data

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

if __name__ == "__main__":
    print("Linked List-based Stack Operations:")
    linked_stack = LinkedListStack()
    linked_stack.push(10)
    linked_stack.push(20)
    linked_stack.push(30)
    print("Peek from Linked List Stack:", linked_stack.peek())
    linked_stack.pop()
    print("Peek after pop from Linked List Stack:", linked_stack.peek())
    print("Is Linked List Stack Empty?", linked_stack.is_empty())
