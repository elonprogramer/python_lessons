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
    
    person = {
        "name": name,
        "tel": tel,
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
        for data_dicts in data:
            data_dict = ",".join(data_dicts)
            print(data_dict)
            print()
            print(data_dicts)


if __name__ == "__main__":
    main()