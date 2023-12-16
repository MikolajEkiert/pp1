import re
def f(first_letter,last_letter):
    with open('data.txt','r', encoding='utf-8') as f:
        f_content=f.read()
        list_of_words=re.findall(fr'\b{first_letter}\w+{last_letter}\b',f_content)
        # with open('pietruszka.txt','w') as result:
        #     words=""
        #     for word in list_of_words:
        #         words+=word+'\n'
        #     result.write(words)
        #     result.write(str(len(list_of_words)))
        return len(list_of_words)
print(f("w", "d"))
