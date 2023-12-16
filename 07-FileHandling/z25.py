import re
message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
day= re.findall(r'\b\w+day\b',message)
avg_temp=(int(temperatures[0])+int(temperatures[1])+int(temperatures[2]))//3
print(avg_temp)
