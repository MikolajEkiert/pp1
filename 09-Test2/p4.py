def f(subjects):
    max_avg=0
    subject=''
    for key, value in subjects.items():
        avg=(sum(value)/len(value))
        if avg>max_avg:
            max_avg=avg
            subject=key
    return subject
print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))