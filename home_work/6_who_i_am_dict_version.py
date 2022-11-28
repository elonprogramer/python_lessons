#Игра кто я?
import time
#как меня зовут?
print("Привет. я помогу тебе всповнить кто ты")
person = {
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
time.sleep(2)
print('Введи имя')
search = input()
if search == 'Юрий' or search == 'Юра':
    print("\n Твое Имя: " + person['yura']['name'] + "\n Твоя фамилия: " + person['yura']['last_name'] + "\n Год рождения : " + person['yura']['year'])
elif search == 'Владислав' or search == 'Влад':
    print("\n Твое Имя: " + person['vlad']['name'] + "\n Твоя фамилия: " + person['vlad']['last_name'] + "\n Год рождения : " + person['vlad']['year'])
else:
    print("Такого увы нет")