class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def tree_height(root):
    if not root:
        return -1
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    return max(left_height, right_height) + 1

# Example usage
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Height of the Tree:", tree_height(root))
