def f(array2d):
    bools=[]
    for array in array2d:
        for number in array:
            try:
                if sum(array2d[number])==sum(array[number] for array in array2d):
                    bools.append(True)
                else:
                    bools.append(False)
            except IndexError:
                continue
    if False in bools:
        return False
    else:
        return True
print(f([[3,7,2],[4,2,5],[5,2,1]]),f([[3,7,2],[4,2,5],[9,2,1]]))
