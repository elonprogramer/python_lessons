import json
from random import choice

def gen_person():
    name = ''
    tel = ''
    letters = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    while len(name) != 5:
        name += choice(letters)
    while len(tel) != 7:
        tel += choice(nums)
    
    #person = {
    #    "name": name,
    #    "tel": tel,
    #}
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
    return person


def write_json(person_dict):
    try:
        data = json.load(open("persons.json"))
    except:
        data = []
    data.append(person_dict)

    with open("persons.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def read_json():
    
    try:
        data = json.load(open("persons.json"))
    except:
        data = []
    return data

def main():
    print("Читать = 1 Писать = 2")
    user_input = int(input())
    if user_input == 2:
        for i in range(5):
            write_json(gen_person())
    elif user_input == 1:
        data = read_json()
        print(data)
#        data = data[0]
#        print(data)
#        person_names_dict = {}
#        search = input()
#        for name_key in data.keys():
#            person_names_dict[data[name_key]['name']] = name_key
#
#        if search in person_names_dict:
#            key_id = person_names_dict[search]
#            print(f"{data[key_id]['last_name']} \n {data[key_id]['surname']} \n {data[key_id]['year']}")
#        else:
#            print("Пользователь не существующет в базе данных")
if __name__ == "__main__":
    main()