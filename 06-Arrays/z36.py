array=[7,3,8,5,2]
def sec_largest():
    for num in array:
        if num==max(array):
            array.remove(num)
            sec_larg=max(array)    
    return sec_larg      
def diff():
    return max(array)-min(array)
def median():
    array.sort()
    if len(array) % 2 == 0:
        mid1 = array[len(array) // 2]
        mid2 = array[len(array) // 2 - 1]
        med = (mid1 + mid2) / 2
    else:
        med = array[len(array) // 2]
    return med
def minmax():
    array2=[min(array),max(array)]
    return array2
def string():
    string=""
    for num in array:
        string+=str(num)+"-"
    return string[:-1]
