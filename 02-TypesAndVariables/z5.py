number=int(input(print("enter the number of purchased products:")))
price=float(input(print('enter the price of one product:')))
if number>2:
    print('number of products:', number ,  "\n product price:", price, "\n to pay:", 2*price+(number-2)*price*0.75 )
else:
    print ('number of products:', number ,  "\n product price:", price, "\n to pay:", number*price)