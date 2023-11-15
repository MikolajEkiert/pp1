"""def f(amount_to_pay):
    while amount_to_pay>0:
        while amount_to_pay>=5:
            return amount_to_pay-5
        while amount_to_pay>=2:
            return amount_to_pay-2
        while amount_to_pay>=1:
            return amount_to_pay-1
print(f(23))"""
def min_coins_to_pay(amount_to_pay):
    # Initialize the count of coins to zero
    coin_count = 0
    
    # Repeatedly use the largest available coin denomination
    while amount_to_pay > 0:
        if amount_to_pay >= 5:
            coin_count += amount_to_pay // 5
            amount_to_pay %= 5
        elif amount_to_pay >= 2:
            coin_count += amount_to_pay // 2
            amount_to_pay %= 2
        else:
            coin_count += amount_to_pay
            amount_to_pay = 0

    return coin_count
print(min_coins_to_pay(23))