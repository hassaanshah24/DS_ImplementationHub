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

def reverse_string(input_string):
    stack = ArrayStack(len(input_string))
    for char in input_string:
        stack.push(char)  # Push each character onto the stack

    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()  # Pop each character to get reversed string

    return reversed_string

if __name__ == "__main__":
    input_string = "Hello, World!"
    print("Original String:", input_string)
    print("Reversed String:", reverse_string(input_string))
