array=[12, 6, 4, 9, 10]
def star():
    for n in array:
        stars=n*'*'
        print(f'{n}: {stars}')
star()