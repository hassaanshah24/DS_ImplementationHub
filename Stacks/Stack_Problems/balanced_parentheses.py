class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.stack) == 0

def is_balanced(expression):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False

    return stack.is_empty()

# Example usage
if __name__ == "__main__":
    expr = "{[()()]}"
    print("Balanced" if is_balanced(expr) else "Not Balanced")
