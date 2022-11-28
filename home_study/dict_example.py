# пример словарей

#luna
#farsh

# weight_luna = 22
# weight_farsh = 30
#
# print(f'{weight_farsh=}')
# weigth = {}
# print(type(weigth))
# print(type(weight_farsh))
#
# weigth['farsh'] = 30
# weigth['luna'] = 22
# print(weigth)

# key   ---  value

surnames = {
    'vitaliy': 'klichko',
    'elon': 'mask',
    'vasya': 'pupkin'
}

name = 'vitaliy'

person = {
    'vitaliy': {
        'fullname': 'vitaliy klichko',
        'year': 1970,
        'rost': 195,
        'weigth': 95,
    },
    'yura': {
        'fullname': 'yury galatsan',
        'year': 2004,
        'rost': 170,
        'weigth': 70,
    }
}


all_name_keys = person.keys()
print(all_name_keys)

if 'yura' in person.keys():
    print('SUCCESS user in list')
else:
    print('ERROR user not in list')

# print(person['yura']['rost'])

# names = ['yura', 'vitaliy']
# for name in names:
#     print(f"FULLNAME =  {person[name]['fullname']},  ROST = {person[name]['rost']}")
#
# # print(person.keys())
