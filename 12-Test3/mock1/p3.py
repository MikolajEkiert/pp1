def f(d):
    values=0
    for value in d.values():
        values+=value
    return len(list(filter(lambda x: d[f'{x}']>values/len(d),d)))
print(f({"LO231":150,"BA787":20,"NZ15":30}))