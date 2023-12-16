with open('n_powers','w') as f:
    for num in range(11):
        f.write(f'{num}, {num**2}, {num**3}\n')