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

    def search(self, value):
        current = self.root
        while current:
            if value == current.data:
                return True
            elif value < current.data:
                current = current.left
            else:
                current = current.right
        return False

# Example usage
if __name__ == "__main__":
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)

    print("Is 10 in the BST?", bst.search(10))
    print("Is 20 in the BST?", bst.search(20))
