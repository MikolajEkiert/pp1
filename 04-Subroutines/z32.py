def f(n1, n2, n3):
    return n1 < 0 or n2 < 0 or n3 < 0

# Test cases
print(f(11, 6, -4))  # True (at least one number is negative)
print(f(5, 4, 14))   # False (none of the numbers is negative)
