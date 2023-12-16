import random
array=[]
x=0
while x<=8:
    array.append(random.randint(1,999))
    x+=1
num=0
print(array)
string='|'
while num<len(array):
    string+=' '+str(array[num])+"|"
    num+=1
print(len(array)*5*'-')
print(string)
print(len(array)*5*'-')