array=[34,7,19,4,21,8]
even=0
x=0
while x<len(array):
    if  array[x-1]%2==0:
        even+=1
    x+=1
print(even)