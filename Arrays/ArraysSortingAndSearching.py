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

    def linear_search(self, value):
        """Linear Search: Search for an element in the array."""
        for i, val in enumerate(self.arr):
            if val == value:
                return i  # Return the index of the element
        return -1  # Element not found

    def binary_search(self, value):
        """Binary Search: Search for an element in a sorted array."""
        low, high = 0, len(self.arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.arr[mid] == value:
                return mid
            elif self.arr[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
        return -1  # Element not found

    def bubble_sort(self):
        """Bubble Sort: Sort the array using Bubble Sort."""
        n = len(self.arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
        print("Array after Bubble Sort:", self.arr)

    def selection_sort(self):
        """Selection Sort: Sort the array using Selection Sort."""
        n = len(self.arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
        print("Array after Selection Sort:", self.arr)

    def insertion_sort(self):
        """Insertion Sort: Sort the array using Insertion Sort."""
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and key < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key
        print("Array after Insertion Sort:", self.arr)

    def merge_sort(self):
        """Merge Sort: Sort the array using Merge Sort."""
        self.arr = self.merge_sort_rec(self.arr)
        print("Array after Merge Sort:", self.arr)

    def merge_sort_rec(self, arr):
        """Helper recursive function for Merge Sort."""
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort_rec(arr[:mid])
        right = self.merge_sort_rec(arr[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        """Helper function to merge two sorted arrays."""
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def quick_sort(self):
        """Quick Sort: Sort the array using Quick Sort."""
        self.quick_sort_rec(0, len(self.arr) - 1)
        print("Array after Quick Sort:", self.arr)

    def quick_sort_rec(self, low, high):
        """Helper function for Quick Sort."""
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort_rec(low, pi - 1)
            self.quick_sort_rec(pi + 1, high)

    def partition(self, low, high):
        """Partition function for Quick Sort."""
        pivot = self.arr[high]
        i = low - 1
        for j in range(low, high):
            if self.arr[j] < pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        return i + 1

    def heap_sort(self):
        """Heap Sort: Sort the array using Heap Sort."""
        n = len(self.arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)
        for i in range(n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.heapify(i, 0)
        print("Array after Heap Sort:", self.arr)

    def heapify(self, n, i):
        """Heapify function for Heap Sort."""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and self.arr[left] > self.arr[largest]:
            largest = left
        if right < n and self.arr[right] > self.arr[largest]:
            largest = right
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(n, largest)


# Example usage
if __name__ == "__main__":
    array = Array()

    # Insert elements into the array
    array.insert(10)
    array.insert(20)
    array.insert(15)
    array.insert(30)
    array.insert(5)

    # Traverse the array
    array.traverse()

    # Searching for elements
    print("Linear Search for 15:", array.linear_search(15))
    print("Binary Search for 15 (before sorting):", array.binary_search(15))

    # Sorting the array using different algorithms
    array.bubble_sort()
    array.selection_sort()
    array.insertion_sort()

    # Reset array for sorting operations
    array.arr = [10, 20, 15, 30, 5]
    array.merge_sort()

    array.arr = [10, 20, 15, 30, 5]
    array.quick_sort()

    array.arr = [10, 20, 15, 30, 5]
    array.heap_sort()

    # Searching after sorting (Binary Search)
    print("Binary Search for 15 (after sorting):", array.binary_search(15))
