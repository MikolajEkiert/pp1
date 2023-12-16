x='An apple a day keeps the doctor away'
array=x.split()
array.sort(key=len, reverse=True)
array.sort()
print(len(array),array,array)