facebook=(input(print('do you have a facebook account:(T/F)')))
twitter=(input(print('do you have a twitter account:(T/F)')))
instagram=(input(print('do you have a instagram account:(T/F)')))
if ((facebook and instagram) or (facebook and twitter) or (twitter and instagram)) == 'T':
    print(" you are a good influencer!")
else :
    print("you are not a good influencer!")