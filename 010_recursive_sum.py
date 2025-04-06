def sum_list(arr):
    if not arr:
        return 0
    last_element = arr.pop()
    return last_element + sum_list(arr)

print(sum_list([1,2,3,4,5]))