array=[2, 3, 2, 5, 8, 1, 9, 8]
ue=""
for x in array:
    if array.count(x)==1:
        ue+=str(x)+", "
print(ue[:-2])