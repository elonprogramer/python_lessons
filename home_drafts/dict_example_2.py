# another examples

# через фигурные скобки
d = {}  # пустой словарь

dogs = {
    'Luna': 22,
    'Farsh': 30
}


# Через функцию dict
another_empty_dict = dict()
print(another_empty_dict)

another_dog = dict(Luna=22, Farsh=30)
print(another_dog)

#  с помощью метода fromkeys:



print('=========== fromkeys========')

dogs_weight_dict = dict.fromkeys(['luna', 'farsh', 'bobik', 'dasha', 'gorga'], 0)

print(dogs_weight_dict)

print('=========== UPDATE ========')

# добавление новых ключей
person_dict = {'yura': 60, 'sasha':80}
print(person_dict)

person_dict['ivan'] = 100
print(person_dict)

person_dict.update({'misha': 140})
print(person_dict)

spain_weights = {
    'serhio': 20,
    'raul': 45,
    'migel': 60
}
person_dict.update(spain_weights)
print(person_dict)

# person_dict.clear()
# print(person_dict)

print(f"Serhio = {person_dict['serhio']}")
# print(f"Dima = {person_dict['dima']}")
# a = None
# if a:
#     print(1)
# else:
#     print(2)

# dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).

res = person_dict.get('dima', 0)
print(res)

# keys() -  возвращает ключи в словаре.

print(person_dict.keys())

# values()

weights_list = person_dict.values()
print(weights_list)

# weight_average = 0
# s = 0
weight_average, s = (0, 0)

print(f'{weight_average=},{s=}')

for w in weights_list:
    s = s + w
weight_average = s / len(weights_list)
print(weight_average)


print('=========== POP ========')
print(person_dict)
w = person_dict.pop('misha')
print(f'{w=}')
print(person_dict)

items = person_dict.items()
print(items)

# ==============================


for k, v in person_dict.items():
    print(f'NAME IS {k}, WEIGHT IS {v}')
