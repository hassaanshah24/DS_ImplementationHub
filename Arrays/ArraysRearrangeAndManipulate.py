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

    def reverse(self):
        """Reverse the array."""
        self.arr.reverse()
        print("Reversed Array:", self.arr)

    def rotate_left(self, k):
        """Rotate the array left by k positions."""
        k = k % len(self.arr)  # To handle rotations larger than the array size
        self.arr = self.arr[k:] + self.arr[:k]
        print(f"Array after rotating left by {k} positions:", self.arr)

    def rotate_right(self, k):
        """Rotate the array right by k positions."""
        k = k % len(self.arr)  # To handle rotations larger than the array size
        self.arr = self.arr[-k:] + self.arr[:-k]
        print(f"Array after rotating right by {k} positions:", self.arr)

    def move_zeros(self, to_end=True):
        """Move all zeros to the end or beginning of the array."""
        non_zeros = [x for x in self.arr if x != 0]
        zeros = [0] * (len(self.arr) - len(non_zeros))
        self.arr = non_zeros + zeros if to_end else zeros + non_zeros
        print(f"Array after moving zeros to the {'end' if to_end else 'beginning'}:", self.arr)

    def rearrange_alternate(self):
        """Rearrange the array to alternate positive and negative elements."""
        positive = [x for x in self.arr if x > 0]
        negative = [x for x in self.arr if x < 0]

        result = []
        i, j = 0, 0
        # Merge positive and negative elements alternately
        while i < len(positive) and j < len(negative):
            result.append(positive[i])
            result.append(negative[j])
            i += 1
            j += 1
        # Append remaining elements if any
        result.extend(positive[i:])
        result.extend(negative[j:])

        self.arr = result
        print("Array after rearranging alternate positives and negatives:", self.arr)

    def rearrange_to_largest(self):
        """Rearrange the array to form the largest possible number."""
        self.arr = sorted(map(str, self.arr), reverse=True)
        print("Array rearranged to form the largest number:", ''.join(self.arr))

    def rearrange_to_smallest(self):
        """Rearrange the array to form the smallest possible number."""
        self.arr = sorted(map(str, self.arr))
        print("Array rearranged to form the smallest number:", ''.join(self.arr))


# Example usage
if __name__ == "__main__":
    array = Array()

    # Insert elements into the array
    array.insert(10)
    array.insert(0)
    array.insert(5)
    array.insert(20)
    array.insert(0)
    array.insert(-10)
    array.insert(15)

    # Traverse the array
    array.traverse()

    # Reverse the array
    array.reverse()

    # Rotate the array left and right
    array.rotate_left(2)
    array.rotate_right(3)

    # Move all zeros to the end and beginning
    array.move_zeros(to_end=True)
    array.move_zeros(to_end=False)

    # Rearrange the array with alternate positive and negative elements
    array.rearrange_alternate()

    # Rearrange to form the largest and smallest number possible
    array.rearrange_to_largest()
    array.rearrange_to_smallest()
