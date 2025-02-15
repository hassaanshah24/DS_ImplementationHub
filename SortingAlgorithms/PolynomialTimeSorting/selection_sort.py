def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap min with first

# Example usage
arr = [29, 10, 14, 37, 14]
selection_sort(arr)
print("Sorted array:", arr)
