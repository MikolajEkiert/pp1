array=[8, 2, 5, 1,9]
def f():
    arraysqr=''
    for x in array:
        arraysqr+=str(x**2)+", "
    return arraysqr[:-2]
print(f())
