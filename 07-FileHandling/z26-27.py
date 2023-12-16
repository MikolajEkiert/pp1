import re
text='To be, or not to be, that is the question'
vowels=re.findall('[aeiouy]',text)
print(len(vowels))
spaces=re.findall(' ',text)
print(len(spaces)+1)
words=re.findall(r'\b\w+\b', text)
print(len(words))
