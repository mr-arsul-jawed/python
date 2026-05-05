def quick_sort(arr):
    # Step 1: Base condition (if list is small, already sorted)
    if len(arr) <= 1:
        return arr

    # Step 2: Choose pivot (we take first element)
    pivot = arr[0]

    # Step 3: Create two empty lists
    left = []   # elements smaller than pivot
    right = []  # elements greater than pivot

    # Step 4: Compare each element with pivot
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    # Step 5: Recursively sort left and right
    return quick_sort(left) + [pivot] + quick_sort(right)


# Example
arr = [8, 3, 1, 7, 0, 10, 2]
print(quick_sort(arr))