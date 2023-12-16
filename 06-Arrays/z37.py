array=[x for x in range(1,101)]
value=int(input('enter a real number: '))
def count_elements_greater_than_value():
    count = 0
    for num in array:
        if num > value:
            count += 1
    return count
print(count_elements_greater_than_value())