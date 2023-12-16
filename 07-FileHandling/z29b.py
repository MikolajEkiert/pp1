import re
with open('grades.txt','r') as grades:
    text=grades.read()
    grades_list=re.findall('[0-9].[0-9]',text)
    num=0
    numerator=0
    while num<len(grades_list):
        numerator+=float(grades_list[num])
        num+=1
    avg=numerator//len(grades_list)
    print(avg)
