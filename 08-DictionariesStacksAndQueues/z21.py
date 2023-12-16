def onp():
    stack = []
    while True:
        char = input('Enter a value to convert:')
        if char.isdigit() or (char[0] == '-' and char[1:].isdigit()):
            stack.append(int(char))
        elif char!='=':           
            if char == '+':
                b = stack.pop()
                a = stack.pop()
                result = a + b
            elif char == '-':
                b = stack.pop()
                a = stack.pop()
                result = a - b
            elif char == '/':
                b = stack.pop()
                a = stack.pop()                
                result = a / b
            elif char == '*':
                b = stack.pop()
                a = stack.pop()
                result = a * b
            stack.append(result)
        if char=='=':
            return stack[0]
print(onp())



            
