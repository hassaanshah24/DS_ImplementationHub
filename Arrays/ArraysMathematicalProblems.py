class Array:
    def __init__(self):
        self.arr = []

    def insert(self, value):
        """Insert an element at the end of the array."""
        self.arr.append(value)

    def delete(self, position):
        """Delete an element from a specific position."""
        if 0 <= position < len(self.arr):
            removed = self.arr.pop(position)
            print(f"Deleted {removed} from position {position}.")
        else:
            print(f"Invalid position: {position}.")

    def traverse(self):
        """Print all elements in the array."""
        print("Array elements:", self.arr)

    def find_max(self):
        """Find the maximum element in the array."""
        if not self.arr:
            print("Array is empty.")
            return None
        return max(self.arr)

    def find_min(self):
        """Find the minimum element in the array."""
        if not self.arr:
            print("Array is empty.")
            return None
        return min(self.arr)

    def calculate_sum(self):
        """Calculate the sum of all elements in the array."""
        return sum(self.arr)

    def calculate_average(self):
        """Calculate the average of all elements in the array."""
        if not self.arr:
            print("Array is empty.")
            return None
        return sum(self.arr) / len(self.arr)

    def find_second_largest(self):
        """Find the second largest element in the array."""
        if len(self.arr) < 2:
            print("Array must have at least two elements.")
            return None
        unique_elements = list(set(self.arr))
        unique_elements.sort()
        return unique_elements[-2] if len(unique_elements) > 1 else None

    def find_second_smallest(self):
        """Find the second smallest element in the array."""
        if len(self.arr) < 2:
            print("Array must have at least two elements.")
            return None
        unique_elements = list(set(self.arr))
        unique_elements.sort()
        return unique_elements[1] if len(unique_elements) > 1 else None

    def is_sorted(self):
        """Check if the array is sorted in ascending order."""
        return self.arr == sorted(self.arr)

    def count_occurrences(self, value):
        """Count occurrences of a specific element."""
        return self.arr.count(value)


# Example usage
if __name__ == "__main__":
    array = Array()

    # Insert elements into the array
    array.insert(10)
    array.insert(20)
    array.insert(15)
    array.insert(30)
    array.insert(5)
    array.insert(20)  # Duplicated element for counting

    # Traverse the array
    array.traverse()

    # Find the maximum and minimum elements
    print("Maximum Element:", array.find_max())
    print("Minimum Element:", array.find_min())

    # Calculate the sum and average of elements
    print("Sum of Elements:", array.calculate_sum())
    print("Average of Elements:", array.calculate_average())

    # Find second largest and second smallest elements
    print("Second Largest Element:", array.find_second_largest())
    print("Second Smallest Element:", array.find_second_smallest())

    # Check if the array is sorted
    print("Is the Array Sorted?", array.is_sorted())

    # Count occurrences of a specific element
    value_to_count = 20
    print(f"Occurrences of {value_to_count}:", array.count_occurrences(value_to_count))
