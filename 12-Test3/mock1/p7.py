def f(arr2D):
    max_value=0
    for arr in arr2D:
        if len(arr)>max_value:
            max_value=len(arr)
    sarray=[0]*max_value
    i=0
    for array in arr2D:
        for number in array:
            sarray[i]+=number
            i+=1
            if i==len(array):
                i=0
    for n in sarray:
        if sarray.count(n)>1:
            return True
        else:
            return False
print(f([[3,4],[5,1],[4,7]]))
