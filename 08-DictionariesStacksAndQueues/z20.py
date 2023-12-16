import stack as s
def binary(number):
    while number>=1:
        remainder=number%2
        s.stack.append(remainder)
        number=number//2
    return s.stack
binary(18)
print(s.stack)
n=0
while n<=len(s.stack)+3:
    print(s.stack.pop())
    n+=1