import z23
text=input('enter a sentence: ')
letter=input('Enter a letter: ')
count = z23.count_letter_occurrences(text, letter)
if __name__=='__main__':
    print(text)
    print(f"The number of letter '{letter}' in {text} is: {count}")