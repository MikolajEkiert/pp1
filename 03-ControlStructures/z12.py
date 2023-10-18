n1=input('enter the name of person one:')
n2=input('enter the name of person two:')
a1=int(input(print('enter the age of person one:')))
a2=int(input(print('enter the age of person two:')))
if a1 and a2 >=18:
    print(f'{n1} and {n2} are adults')
else:
    print('at least one person is not an adult')