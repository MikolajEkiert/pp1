with open('textfile.txt','w') as f:
    i=1
    while i<=50:
        f.write(f'{str(i)}\n')
        i+=1