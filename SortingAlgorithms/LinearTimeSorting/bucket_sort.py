def bucket_sort(arr, bucket_size=5):
    if len(arr) == 0:
        return arr

    # Step 1: Find the minimum and maximum values
    min_value, max_value = min(arr), max(arr)

    # Step 2: Determine the number of buckets
    bucket_count = (max_value - min_value) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    # Step 3: Place elements into respective buckets
    for num in arr:
        index = (num - min_value) // bucket_size
        buckets[index].append(num)

    # Step 4: Sort each bucket and concatenate results
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))  # Using Python's built-in sorting

    return sorted_array

# Example usage
if __name__ == "__main__":
    arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
    sorted_arr = bucket_sort(arr, bucket_size=0.1)
    print("Sorted array:", sorted_arr)
