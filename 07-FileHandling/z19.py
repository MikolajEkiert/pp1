source= open("ft.txt")
with open('ft3.txt','w') as destination:
    for line in source:
        destination.write(line)
source.close()
