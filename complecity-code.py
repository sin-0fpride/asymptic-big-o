import math

# O(1) - Constant time
def constant_time(arr):
    return arr[0]  # Always one operation

# O(log n) - Logarithmic time
def logarithmic_time(n):
    while n > 1:
        n = n // 2  # Cuts input in half each time

# O(n) - Linear time
def linear_time(arr):
    for item in arr:
        print(item)  # One operation per item

# O(n log n) - Linearithmic time
def linearithmic_time(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = linearithmic_time(arr[:mid])
    right = linearithmic_time(arr[mid:])
    return merge(left, right)  # Merge sort

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:] + right[j:])
    return result

# O(n^2) - Quadratic time
def quadratic_time(arr):
    for i in arr:
        for j in arr:
            print(i, j)  # Nested loop

# O(n^k) - Polynomial time (e.g. k = 3)
def cubic_time(arr):
    for i in arr:
        for j in arr:
            for k in arr:
                print(i, j, k)  # 3 nested loops