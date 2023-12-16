names=['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
max=0
for x in names:
    if len(x)>max:
        max=len(x)
        max_name=x
print(f'longest name in the array is: {max_name}')
