def f(n):
    sn=str(n)
    array=[]
    for num in sn:
        if int(num)%2==1:
            array.append(int(num))
    if len(array)==0:
        return -1
    else:
        max_arr=max(array)
        min_arr=min(array)
        return max_arr-min_arr
print(f(10852))
print(f(7235973))
print(f(4388))
print(f(846206))