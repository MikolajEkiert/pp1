array=[2,3,7,5,4]
middle=len(array)//2
middle_value=array[middle]
values=''
halfstr=''
for x in array:
    values+=str(x)+' '
half_array=array[:len(array)//2]
for x in half_array:
    halfstr+=str(x)+' '
print(array,len(array),array[0],array[1],array[-1],"\n",values,array[0:len(array)-1])
print(middle_value,array[0]+array[-1],halfstr)