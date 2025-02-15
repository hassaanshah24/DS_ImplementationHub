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

    def find_min(self, root):
        current = root
        while current.left:
            current = current.left
        return current.data

    def find_max(self, root):
        current = root
        while current.right:
            current = current.right
        return current.data

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

    print("Minimum value in BST:", bst.find_min(bst.root))
    print("Maximum value in BST:", bst.find_max(bst.root))
