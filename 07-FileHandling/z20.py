f=open('meatandfish.txt','w')
mnf=['Skinless white meat','Tuna fish','Luncheon meat','Lean cuts of red meat']
n=0
while n<len(mnf):
    f.write(f'{mnf[n]}\n')
    n+=1
with open('shopping.txt', 'w') as f1:
    n=0
    while n<len(mnf):
        f1.write(f'{mnf[n]}\n')
        n+=1
f.close()