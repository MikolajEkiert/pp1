import re
def f(vname):
    x=re.findall(r'^[a-zA-Z_][a-zA-Z0-9_]{0,4}$',vname)
    if x:
        return True
    else:
        return False
    
print(f("_aB8_"))