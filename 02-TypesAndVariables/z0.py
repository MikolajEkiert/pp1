speed_limit = 140
car_speed = int( input('Enter car speed km/h: ') )

if car_speed > speed_limit:
    print('Warning: speed limit exceeded!!')
else:
    print('You are driving below the speed limit.')
