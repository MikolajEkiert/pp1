p_price= 200
price=int(input(print('enter the prodct \'s price')))
sale=(1-(price/p_price))*100
if sale>0.1:
    print("buy the product!! \n it is", round(sale, 0) , "%", "off")
