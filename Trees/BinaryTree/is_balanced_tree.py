class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def is_balanced(root):
    def check_height(node):
        if not node:
            return 0
        left_height = check_height(node.left)
        right_height = check_height(node.right)
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    return check_height(root) != -1

# Example usage
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Is the tree balanced?", is_balanced(root))
