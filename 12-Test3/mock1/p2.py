def f(x,y,d):
    arr=[]
    for number in range(x,y+1):
        arr.append(str(number))
    for element in arr:
        if d in element:
            return True
        else:
            continue
    return False
print(f(205,210,"04"))