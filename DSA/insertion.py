def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i] #11
        j = i - 1    #0 values = 12

        while j >= 0 and arr[j] > key: 
            arr[j + 1] = arr[j] 
            j -= 1

        arr[j + 1] = key

    return arr

mylist = [12, 11, 13, 5, 6]
print(insertion_sort(mylist))
