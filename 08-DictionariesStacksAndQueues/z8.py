person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }
print(person)
print(person['name'], person["hobby"])
person["surname"]='Nowak'
print(person["surname"])
person['married']=False
print(person['married'])
person['gender']='male'
person['hobby']+=['bicycle']
print(person['gender'],person['hobby'])
person['phone'].update({'work phone': '313131444'})
print(person['phone'])