def numbers(n):
    x=''
    for i in range(1,n+1):
            x=x+str(i)+ " "
    print(f'Numbers <1,{n}>:', x)
numbers(15)
numbers(7)