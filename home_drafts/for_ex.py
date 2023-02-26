lists = ['1', '2', '3', '4', '5', '6', '7', '8']

for a in lists:
    print(a, end=' ')
    print()

dict = {'a': 1, 'b': 2, 'c': 3}

for k, v in dict.items():
    print(k, v, end=' ')
    print()
    print(v)

dict_list = {'a': ['1','2', '3'], 'b': ['4', '5', '6'], 'c': ['7', '8', '9']}

for key, value in dict_list.items():
    for item in value:
        print()
        print(item, )
        print()
        print('key: ' + key + 'value: ', end=' ')
        print(value, end=' ')

list_dict = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}]

for item in list_dict:
    for key, value in item.items():
        print(f"key: {key} value: {value}")
        print(f'a = {item["a"]}, b = {item["b"]}')
