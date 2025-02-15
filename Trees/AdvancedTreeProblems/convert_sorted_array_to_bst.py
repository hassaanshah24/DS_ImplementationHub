class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def sorted_array_to_bst(arr, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    root = Node(arr[mid])

    root.left = sorted_array_to_bst(arr, start, mid - 1)
    root.right = sorted_array_to_bst(arr, mid + 1, end)

    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

# Example usage
if __name__ == "__main__":
    sorted_arr = [-10, -3, 0, 5, 9]
    bst_root = sorted_array_to_bst(sorted_arr, 0, len(sorted_arr) - 1)

    print("Inorder Traversal of Balanced BST:")
    inorder_traversal(bst_root)
