# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i #5
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]: # 2 < 5
#                 min_index = j # min_index = 1 value = 2
#         arr[i], arr[min_index] = arr[min_index], arr[i] # arr[0], arr[1] = arr[1], arr[0] => 5, 2 = 2, 5

#     return arr


# # mylist = [64, 34, 25, 12, 22, 11, 90, 5]
# mylist = [5, 2]
# print(selection_sort(mylist))


