class ArrayStack:
    def __init__(self, capacity):
        self.stack = [None] * capacity
        self.top = -1
        self.capacity = capacity

    def push(self, value):
        """Push an element onto the stack."""
        if self.top == self.capacity - 1:
            print("Stack is full!")
            return
        self.top += 1
        self.stack[self.top] = value
        print(f"Pushed {value} onto array stack.")

    def pop(self):
        """Pop an element from the stack."""
        if self.top == -1:
            print("Stack is empty!")
            return None
        value = self.stack[self.top]
        self.top -= 1
        print(f"Popped {value} from array stack.")
        return value

    def peek(self):
        """View the top element of the stack."""
        if self.top == -1:
            print("Stack is empty!")
            return None
        return self.stack[self.top]

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top == -1

    def is_full(self):
        """Check if the stack is full."""
        return self.top == self.capacity - 1

if __name__ == "__main__":
    print("Array-based Stack Operations:")
    array_stack = ArrayStack(5)
    array_stack.push(10)
    array_stack.push(20)
    array_stack.push(30)
    array_stack.push(40)
    array_stack.push(50)
    array_stack.push(60)  # Should show "Stack is full!"
    print("Peek from Array Stack:", array_stack.peek())
    array_stack.pop()
    print("Peek after pop from Array Stack:", array_stack.peek())
    print("Is Array Stack Empty?", array_stack.is_empty())
