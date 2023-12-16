import random as r
with open('numbers.txt','w') as f:
    n=1
    while n<=50:
        f.write(f'{r.randint(100,999)}\n')
        n+=1