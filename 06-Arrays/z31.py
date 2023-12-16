array=[3,1,2,4]
def occurs(number):
    if number in array:
        return f'Number: {number}\nArray:{array}\nResult: Number {number} apears in the array'
print(occurs(3))