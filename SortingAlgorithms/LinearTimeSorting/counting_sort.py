def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    for num in arr:
        count[num] += 1

    index = 0
    for i in range(len(count)):
        while count[i] > 0:
            output[index] = i
            index += 1
            count[i] -= 1

    return output

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
print("Sorted array:", counting_sort(arr))
