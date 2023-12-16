with open('numbers.txt','r') as f:
    sum=0
    for number in f:
        sum+=int(number)
print(sum)