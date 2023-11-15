def f(x,y):
    number_sum=0
    for number in range(x,y):
        if number<0 and number%2==0:
            number_sum+=1
    return number_sum
print(f(-7,8))
