array=[34,7,19,4,21,8]
even=0
for x in array:
    if x%2==0:
        even+=1
    else:
        continue
print(even)