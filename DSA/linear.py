def  search(arr, x):
    for i , value in enumerate(arr):
        if value == x:
            return i
    return -1


arr = [2,3,4,10,40]
x = 10

result = search(arr, x)
if result != -1:
    print("Element is present at index", str(result))
else:    
    print("Element is not present in array")