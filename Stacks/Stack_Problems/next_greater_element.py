def next_greater_element(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result

# Example usage
if __name__ == "__main__":
    arr = [4, 5, 2, 10, 8]
    print("Array:", arr)
    print("Next Greater Element:", next_greater_element(arr))
