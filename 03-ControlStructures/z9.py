correct=60
full_points=75
if correct/full_points>=0.5:
    print("you\'ve passed the test")
elif correct/full_points>1 or correct/full_points<0:
   print("enter a real score")

else:
    print('you\'ve failed to pass')