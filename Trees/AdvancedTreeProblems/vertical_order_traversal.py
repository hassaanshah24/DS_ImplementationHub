from collections import deque, defaultdict

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def vertical_order_traversal(root):
    if not root:
        return

    column_table = defaultdict(list)
    queue = deque([(root, 0)])

    while queue:
        node, column = queue.popleft()
        column_table[column].append(node.data)

        if node.left:
            queue.append((node.left, column - 1))
        if node.right:
            queue.append((node.right, column + 1))

    for col in sorted(column_table.keys()):
        print(column_table[col])

# Example usage
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Vertical Order Traversal:")
    vertical_order_traversal(root)
