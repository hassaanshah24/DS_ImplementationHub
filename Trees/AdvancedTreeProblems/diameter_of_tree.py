class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def diameter(root):
    def height_and_diameter(node):
        if not node:
            return 0, 0
        left_height, left_diameter = height_and_diameter(node.left)
        right_height, right_diameter = height_and_diameter(node.right)
        current_diameter = left_height + right_height
        return max(left_height, right_height) + 1, max(current_diameter, left_diameter, right_diameter)

    return height_and_diameter(root)[1]


# Example usage
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Diameter of the Tree:", diameter(root))
