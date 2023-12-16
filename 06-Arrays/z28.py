array1=[4,36,12,28,9,44,5]
array2=[5,1,36]
x=0
numbers=''
while x<len(array1):
    if array1[x] not in array2:
        numbers+=str(array1[x])+', '
    x+=1
print(numbers[:-2])
        