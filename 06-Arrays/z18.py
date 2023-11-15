array= [[True,False],[True,True],[False,False]]
for rows in range(len(array)):
    for number in range(len(array[rows])):
        if array[rows][number]==True:
            array[rows][number]=False
        else:
            array[rows][number]=True
        number+=1
    rows+=1
print(array)