class Array:
    def __init__(self):
        self.arr = []

    def insert(self, value, position=None):
        """Insert an element at a specific position (or at the end if position is None)."""
        if position is None:
            self.arr.append(value)
            print(f"Inserted {value} at the end.")
        elif 0 <= position <= len(self.arr):
            self.arr.insert(position, value)
            print(f"Inserted {value} at position {position}.")
        else:
            print(f"Invalid position: {position}.")

    def delete(self, position):
        """Delete an element from a specific position."""
        if 0 <= position < len(self.arr):
            removed = self.arr.pop(position)
            print(f"Deleted {removed} from position {position}.")
        else:
            print(f"Invalid position: {position}.")

    def search(self, value):
        """Search for an element in the array."""
        if value in self.arr:
            position = self.arr.index(value)
            print(f"Element {value} found at position {position}.")
        else:
            print(f"Element {value} not found.")

    def traverse(self):
        """Print all elements in the array."""
        if self.arr:
            print("Array elements (detailed):")
            for i, value in enumerate(self.arr):
                print(f"Index {i}: {value}")
            print("Array elements (full array):", self.arr)
        else:
            print("The array is empty.")

# Example usage
if __name__ == "__main__":
    array = Array()

    # Insert elements
    array.insert(10)
    array.insert(20)
    array.insert(15, 1)

    # Traverse
    array.traverse()

    # Search for an element
    array.search(15)
    array.search(100)

    # Delete an element
    array.delete(1)
    array.traverse()

    # Attempt invalid operations
    array.insert(25, 10)  # Invalid position
    array.delete(10)  # Invalid position
