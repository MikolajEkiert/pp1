def f(card_number):
    if len(card_number)==16:
        print(f'{card_number[slice(2)]}**********{card_number[slice(12,16)]}')
    else:
        print('invalid card number')

