def f(binary_number):
    for n in binary_number:
        if n=='0' or n=='1':
            continue
        else:
            return False
    return True
print(f("101101"))
            