array=[x for x in range(1,11)]
array2=[]
for num in array:
    if num%2==0:
        array2.append(num)
for num in array:
    if num%2==1:
        array2.append(num)
print(array2)
