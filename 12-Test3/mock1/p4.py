def f(fnc,res):
    diff=max(list(filter(fnc,res)))-min(list(filter(fnc,res)))
    return diff
print(f(lambda x: x>30 and x<90,[95,90,20,50,70]))