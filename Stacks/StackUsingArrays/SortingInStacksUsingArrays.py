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

    def pop(self):
        """Pop an element from the stack."""
        if self.top == -1:
            print("Stack is empty!")
            return None
        value = self.stack[self.top]
        self.top -= 1
        return value

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top == -1

def sort_stack_non_recursive(stack):
    """Sort a stack without recursion."""
    helper_stack = ArrayStack(stack.capacity)
    while not stack.is_empty():
        temp = stack.pop()

        while not helper_stack.is_empty() and helper_stack.stack[helper_stack.top] > temp:
            stack.push(helper_stack.pop())

        helper_stack.push(temp)

    # Transfer back to the original stack
    while not helper_stack.is_empty():
        stack.push(helper_stack.pop())

if __name__ == "__main__":
    stack = ArrayStack(5)
    stack.push(30)
    stack.push(10)
    stack.push(50)
    stack.push(20)
    stack.push(40)

    print("Original Stack:")
    while not stack.is_empty():
        print(stack.pop(), end=" ")

    # Adding items again to sort
    stack.push(30)
    stack.push(10)
    stack.push(50)
    stack.push(20)
    stack.push(40)

    # Sort the stack without recursion
    sort_stack_non_recursive(stack)

    print("\nSorted Stack:")
    while not stack.is_empty():
        print(stack.pop(), end=" ")
