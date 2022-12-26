person = {
    '1': {
        'name' : 'Юрий',
        'last_name' : 'Галацан',
        'surname' : 'Владимирович',
        'year' : '2004',
    },
    '2': {
        'name' : 'Владислав',
        'last_name' : 'Галацан',
        'surname' : 'Владимирович',
        'year' : '2011',
    },
    '3': {
        'name' : 'Василий',
        'last_name' : 'Галацан',
        'surname' : 'Владимирович',
        'year' : '2011',
    }
}
person_names_dict = {}
search = input()
for name_key in person.keys():
    person_names_dict[person[name_key]['name']] = name_key

if search in person_names_dict:
    key_id = person_names_dict[search]
    print(person[key_id]['last_name'])
else:
    print("Пользователь не существующет в базе данных")