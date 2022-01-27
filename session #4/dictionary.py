
# dictionaries

person = {
    "first_name": '',
    "last_name": '',
    "age": '',
}

person['first_name'] = input('First Name: ')
person['last_name'] = input('Last Name: ')
person['age'] = input('Age: ')

for k, v in person.items():
    print(k, ':', v)