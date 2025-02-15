import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

# Example usage
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr)
print("Sorted array:", sorted_arr)
