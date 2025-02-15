from collections import deque


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def level_order_traversal(root):
    if not root:
        return

    queue = deque([root])

    while queue:
        current = queue.popleft()
        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


# Example usage
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Level Order Traversal:")
    level_order_traversal(root)
