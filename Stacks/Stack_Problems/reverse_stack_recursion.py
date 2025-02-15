class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if not self.is_empty() else None

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.stack) == 0

    def insert_at_bottom(self, item):
        if self.is_empty():
            self.push(item)
        else:
            temp = self.pop()
            self.insert_at_bottom(item)
            self.push(temp)

    def reverse(self):
        if not self.is_empty():
            temp = self.pop()
            self.reverse()
            self.insert_at_bottom(temp)

    def display(self):
        print(self.stack)

# Example usage
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    print("Original Stack:")
    s.display()

    s.reverse()

    print("Reversed Stack:")
    s.display()
