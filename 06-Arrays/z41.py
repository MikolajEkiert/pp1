import random as r
def rand_elem(array):
    return array[r.randint(0,len(array)-1)]
print(rand_elem(array=[1,2,3,4,5]))
