import re
with open('meatandfish.txt','r') as f:
    text=f.read()
    six_letter_words=re.findall(r'\w{6,}',text)
    print(six_letter_words)