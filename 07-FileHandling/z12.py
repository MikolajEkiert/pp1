name = input("Enter your name: ")
surname = input("Enter your surname: ")
university = input("Enter your university name: ")
field_of_study = input("Enter your field of study: ")
with open('personal_info.txt', 'w') as file:
    file.write(f"Name: {name}\n")
    file.write(f"Surname: {surname}\n")
    file.write(f"University: {university}\n")
    file.write(f"Field of Study: {field_of_study}\n")