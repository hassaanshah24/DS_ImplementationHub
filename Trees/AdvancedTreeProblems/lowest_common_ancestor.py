class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def lowest_common_ancestor(root, p, q):
    if not root:
        return None

    if root.data > p and root.data > q:
        return lowest_common_ancestor(root.left, p, q)
    elif root.data < p and root.data < q:
        return lowest_common_ancestor(root.right, p, q)
    else:
        return root

# Example usage
if __name__ == "__main__":
    root = Node(6)
    root.left = Node(2)
    root.right = Node(8)
    root.left.left = Node(0)
    root.left.right = Node(4)
    root.right.left = Node(7)
    root.right.right = Node(9)

    lca = lowest_common_ancestor(root, 2, 8)
    print("Lowest Common Ancestor:", lca.data)
