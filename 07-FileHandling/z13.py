ft=["The Shawshank Redemption","Inception","The Dark Knight","Pulp Fiction","The Matrix"]
with open('ft.txt','w') as f:
    for num in range(len(ft)):
        f.write(f'{ft[num]}\n')