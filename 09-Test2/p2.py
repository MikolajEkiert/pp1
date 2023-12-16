def f(arr):
    max_value=max(arr)
    min_value=min(arr)
    if arr.count(max_value)>1:
        return min_value
    else:
        return max_value
print(f([5,7,5,5,5,5]))