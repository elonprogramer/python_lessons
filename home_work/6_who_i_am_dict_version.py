#Игра кто я?
import time
persons = {
    'yura': {
        'name' : 'Юрий',
        'last_name' : 'Галацан',
        'surname' : 'Владимирович',
        'year' : '2004',
    },
    'vlad': {
        'name' : 'Владислав',
        'last_name' : 'Галацан',
        'surname' : 'Владимирович',
        'year' : '2011',
    }
}
#как меня зовут?
print("Во что играем? ")
time.sleep(2)
print("Я знаю имя - s я знаю фамилию - n я знаю год рождения = y")
catch = input ()
if catch == "n":
    print("Введи фамилию")
    search = input()
    for key, value in persons.items():
        tex = persons[key]['last_name']
        if search in tex:
            print('Ваше имя : ' + persons[key]['name'] + ', Ваша фамилия: ' + persons[key]['last_name'] + ', Год рождения: ' + persons[key]['year'])
            break 
elif catch == "s":
    print("Введи имя")
    search = input()
    for key, value in persons.items():
        tex = persons[key]['name']
        if search in tex:
            print('Ваше имя : ' + persons[key]['name'] + ', Ваша фамилия: ' + persons[key]['last_name'] + ', Год рождения: ' + persons[key]['year'])
            break
elif catch == "y":
    print("Введи Год")
    search = input()
    for key, value in persons.items():
        tex = persons[key]['year']
        if search in tex:
            print('Ваше имя : ' + persons[key]['name'] + ', Ваша фамилия: ' + persons[key]['last_name'] + ', Год рождения: ' + persons[key]['year'])
            break