# 27. Define a function compare(array1, array2) that returns True if both arrays are the same or False otherwise.  
# Two arrays are the same if they have the same number of elements and values of elements in cells of arrays with the same index are equal.
# Then create a program and try to compare the following arrays: 
#     a. ["water","book","sky"]   ["water","book","sky"]
#     b. [True,False]   [True,False,True]
#     c. [5,3,1]   [5,3,1]
#     d. [3,2,1]   [3,2]
array1=[True,False]
array2=[True,False,True]
def compare(array1, array2):
    if array1==array2:
        return f'array1:{array1}\n array2:{array2}\ncomparison: they are the same'
    else:
        return f'array1:{array1}\n array2:{array2}\ncomparison: they are not the same'
print(compare(array1,array2))