ean= input(print('Enter the EAN cod:'))
if len(ean)==13:
    if ean[0:3] == "590":
        print('This article is from poland')
    else:
        print('This article is from the EU, but not from Poland')
else:
    print('Invalid EAN code')
        