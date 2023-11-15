"""def f(n):
    for number in range(1,n+1):
        number+=str(number)
    return str(number)
print(f(10))"""
def f(n):
    if n <= 0:
        return ""
    
    result = ""
    for i in range(1, n + 1):
        i+=1
        result += str(i-1)
    
    return result

# Test cases
print(f(11))  # Output: "1234567891011"
print(f(4))   # Output: "1234"
