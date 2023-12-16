with open('ft.txt','rb') as source:
    content=source.read()
    with open('ft2.txt','wb') as destination:
        destination.write(content)