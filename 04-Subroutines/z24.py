def in_range(a,x,b):
    return a<=x<=b
x=int(input('Enter a number: '))
a=2
b=15
print(f'A number{x}\n Number {x} is in the range <{a},{b}>: {bool(in_range(a,x,b))}')




