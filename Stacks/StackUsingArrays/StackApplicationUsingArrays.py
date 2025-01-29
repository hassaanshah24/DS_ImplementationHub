# 1. Next Greater Element for Each Element in an Array
def next_greater_element(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)

    return result


# 2. Stock Span Problem
def stock_span(arr):
    stack = []
    result = []

    for i, price in enumerate(arr):
        while stack and arr[stack[-1]] <= price:
            stack.pop()

        span = i + 1 if not stack else i - stack[-1]
        result.append(span)
        stack.append(i)

    return result


# 3. Rainwater Trapping Problem
def rainwater_trapping(arr):
    n = len(arr)
    left_max = [0] * n
    right_max = [0] * n
    water = 0

    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], arr[i])

    right_max[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], arr[i])

    for i in range(n):
        water += min(left_max[i], right_max[i]) - arr[i]

    return water


# 4. Celebrity Problem
def celebrity(matrix):
    stack = list(range(len(matrix)))

    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()
        if matrix[a][b] == 1:
            stack.append(b)
        else:
            stack.append(a)

    celebrity = stack.pop()
    for i in range(len(matrix)):
        if i != celebrity and (matrix[celebrity][i] == 1 or matrix[i][celebrity] == 0):
            return -1
    return celebrity


# 5. Histogram Area Problem
def largest_histogram_area(arr):
    stack = []
    max_area = 0
    index = 0

    while index < len(arr):
        if not stack or arr[stack[-1]] <= arr[index]:
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            area = (arr[top_of_stack] *
                    ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)

    while stack:
        top_of_stack = stack.pop()
        area = (arr[top_of_stack] *
                ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)

    return max_area


if __name__ == "__main__":
    # Test Next Greater Element
    arr1 = [88,34,54,12]
    print("Next Greater Element:", next_greater_element(arr1))

    # Test Stock Span
    arr2 = [12,23,34,45,56]
    print("Stock Span:", stock_span(arr2))

    # Test Rainwater Trapping
    arr3 = [3, 0, 0, 2, 0, 4]
    print("Rainwater Trapped:", rainwater_trapping(arr3))

    # Test Celebrity Problem
    matrix = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 1, 0]
    ]
    print("Celebrity is:", celebrity(matrix))

    # Test Histogram Area Problem
    arr4 = [2, 1, 5, 6, 2, 3]
    print("Maximum Area in Histogram:", largest_histogram_area(arr4))
