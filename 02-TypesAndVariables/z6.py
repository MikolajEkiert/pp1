car_speed= int(input(print('enter the car\'s speed:')))
speed_limit_min=40
speed_limit_max=140
if car_speed>=speed_limit_min and car_speed<=speed_limit_max:
    print("legal car speed")
else:
    print ("invalid car speed")
