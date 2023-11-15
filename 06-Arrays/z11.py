months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def f(n):
    if n<=12:
        return months[n-1]
print(f(1),f(9),f(12))