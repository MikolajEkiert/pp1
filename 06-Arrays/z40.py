array1=[1,2,3,4,5,6]
array2=[1,2,3,4,5,6]
count=0
for x in array1:
    if x in array2:
        count+=1
if count==len(array1):
    print('array 1 is a subset of array 2')