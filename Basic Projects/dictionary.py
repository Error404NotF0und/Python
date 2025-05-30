empty_dict = {}


integer_dict = {1: 'apple', 2: 'ball'}


mixed_dict = {'name': 'John', 1: [2,4,3]}

mixed2_dict = {'name': 'Jack', 'age': 26}

print(mixed2_dict.get('name'))
print(mixed2_dict.get('age'))



mixed2_dict['age'] = 27
print(mixed2_dict)

mixed2_dict['Address'] = 'Downtown'
print(mixed2_dict)

mixed_dict.pop('age')
print(mixed2_dict)

print("Address :", mixed2_dict.get('address'))

mixed_dict.clear()
print(mixed_dict)



