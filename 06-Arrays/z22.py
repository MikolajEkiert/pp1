array=[-15, 8, -31, 47, -2, 19]
def f():
    max=float('-inf')
    min=float('inf')
    for x in range(len(array)):
        if array[x]>max:
            max=array[x]
        elif array[x]<min:
            min=array[x]
    return f'max value={max},\nmin value={min}'
print(f())