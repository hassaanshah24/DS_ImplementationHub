import heapq

class Array:
    def __init__(self):
        self.arr = []

    def insert(self, value):
        """Insert an element at the end of the array."""
        self.arr.append(value)

    def traverse(self):
        """Print all elements in the array."""
        print("Array elements:", self.arr)

    def max_product_of_two(self):
        """Find the maximum product of two numbers."""
        self.arr.sort()
        return self.arr[-1] * self.arr[-2]

    def max_product_of_three(self):
        """Find the maximum product of three numbers."""
        self.arr.sort()
        return max(self.arr[0] * self.arr[1] * self.arr[-1], self.arr[-1] * self.arr[-2] * self.arr[-3])

    def merge_sorted_arrays(self, arr2):
        """Merge two sorted arrays."""
        merged_array = []
        i, j = 0, 0
        while i < len(self.arr) and j < len(arr2):
            if self.arr[i] < arr2[j]:
                merged_array.append(self.arr[i])
                i += 1
            else:
                merged_array.append(arr2[j])
                j += 1
        merged_array.extend(self.arr[i:])
        merged_array.extend(arr2[j:])
        return merged_array

    def find_median_of_two_sorted_arrays(self, arr2):
        """Find the median of two sorted arrays."""
        merged_array = self.merge_sorted_arrays(arr2)
        n = len(merged_array)
        if n % 2 == 1:
            return merged_array[n // 2]
        else:
            return (merged_array[n // 2 - 1] + merged_array[n // 2]) / 2

    def smallest_range(self, k_sorted_arrays):
        """Find the smallest range that includes elements from k sorted arrays."""
        heap = []
        max_value = float('-inf')

        # Initialize the heap with the first element from each array
        for i in range(len(k_sorted_arrays)):
            heapq.heappush(heap, (k_sorted_arrays[i][0], i, 0))
            max_value = max(max_value, k_sorted_arrays[i][0])

        min_range = float('inf')
        start, end = 0, 0

        while True:
            min_value, list_idx, element_idx = heapq.heappop(heap)

            # Update the range if a smaller range is found
            if max_value - min_value < min_range:
                min_range = max_value - min_value
                start, end = min_value, max_value

            # If we reach the end of any list, break (no valid range exists)
            if element_idx + 1 == len(k_sorted_arrays[list_idx]):
                break

            # Push the next element from the same list into the heap
            next_element = k_sorted_arrays[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_element, list_idx, element_idx + 1))

            # Update the max value if necessary
            if next_element > max_value:
                max_value = next_element

        return start, end


# Example usage
if __name__ == "__main__":
    array1 = Array()
    array1.insert(1)
    array1.insert(10)
    array1.insert(5)
    array1.insert(-2)
    array1.insert(7)
    array1.insert(3)

    # Traverse the array
    array1.traverse()

    # Find maximum product of two numbers
    print("Maximum product of two numbers:", array1.max_product_of_two())

    # Find maximum product of three numbers
    print("Maximum product of three numbers:", array1.max_product_of_three())

    # Merge two sorted arrays
    array2 = Array()
    array2.insert(2)
    array2.insert(4)
    array2.insert(6)
    merged = array1.merge_sorted_arrays(array2.arr)
    print("Merged sorted array:", merged)

    # Find the median of two sorted arrays
    median = array1.find_median_of_two_sorted_arrays(array2.arr)
    print("Median of two sorted arrays:", median)

    # Find the smallest range that includes elements from k sorted arrays
    k_sorted_arrays = [
        [4, 10, 15],
        [1, 5, 8],
        [2, 6, 9]
    ]
    smallest_range = array1.smallest_range(k_sorted_arrays)
    print("Smallest range:", smallest_range)
