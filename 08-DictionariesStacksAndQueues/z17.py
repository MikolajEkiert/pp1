import json as j
with open('euro.json','r')as eur:
    data=j.load(eur)
    print(f'Date            Buying Rate     Selling Rate \n============================================')
    rates=data['rates']
    for line in rates:
        print(line['effectiveDate'],"       ", line['ask'],'      ' ,line['bid'])
