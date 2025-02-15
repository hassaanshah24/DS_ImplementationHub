class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        current = self.root
        while True:
            if value < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value)
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(value)
                    return

    def delete(self, root, value):
        if root is None:
            return root
        if value < root.data:
            root.left = self.delete(root.left, value)
        elif value > root.data:
            root.right = self.delete(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            min_val = self.find_min(root.right)
            root.data = min_val
            root.right = self.delete(root.right, min_val)
        return root

    def find_min(self, root):
        current = root
        while current.left:
            current = current.left
        return current.data

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.data, end=" ")
            self.inorder_traversal(root.right)


# Example usage
if __name__ == "__main__":
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    print("BST before deletion:")
    bst.inorder_traversal(bst.root)

    bst.root = bst.delete(bst.root, 50)

    print("\nBST after deleting 50:")
    bst.inorder_traversal(bst.root)
