import time


def start():
    print("Привет.В прошлой части ты обокрал страну драконов")
    time.sleep(1)
    print("Пока ты тратил свои деньги, драконы подали в суд и выиграли дело")
    time.sleep(1)
    print("Твое наказание - Восcтановить экономику страны драконов!")


def signup():
    user_login = input("Введи имя: ")
    user_password = input("Введи пароль: ")
    second_password = input("Повтори пароль: ")
    while_pass = True
    while while_pass:
        if user_password != second_password:
            print("Пароли не совпадают")
            second_password = input("Повтори пароль: ")
        elif user_password == second_password:
            while_pass = False
    user_id = 0
    user_id = user_id + 1
    # user_data = str(f"id = {id} \n name = {user_login} \n password = {second_password}")

    user_data = str(f"{user_id} {user_login} {second_password} 0 50 100 6\n")
    # TODO написать тут функцию
    # get_number_of_users()  которая будет лежать в muduls.py  и которая будет открывать файл на чтение
    # и возвращать количество строк в файле, так чтобы мы могли считать id нового пользователя

    # file = open("/home/elon/python_lessons/home_drafts/Apps/dragon_city/logins.txt", "a")
    file = open("./logins.txt", "a")

    file.write(user_data)
    file.close()


def login():
    user_login = input("Введи имя: ")
    user_password = str(input("Введи пароль: "))
    # file = open("/home/elon/python_lessons/home_drafts/Apps/dragon_city/logins.txt", "r")
    file_logins = open("./logins.txt", "r")
    login_pass_dict = {}

    user_logins_list = file_logins.read().splitlines()
    for line in user_logins_list:
        print(f'---{line}---')
        fields = line.split(' ')
        print(f'name = {fields[1]}')
        login_pass_dict[fields[1]] = fields[2]

    print(login_pass_dict)

    if user_login in login_pass_dict.keys():
        print(f'WE HAVE USER {user_login}')
        if user_password == login_pass_dict[user_login]:
            print(f'Авторизация прошла успешно {user_login}')
            return True
        else:
            print('Пароль неверный')

    else:
        print(f'NO SUCH USER {user_login}')

    # if user_login in file and user_password in file:
    #     print(f"Поздравляю, {user_login}, Ты успешно авторизован!")
    # elif user_login not in file:
    #     print("Ты ввёл не правильный логин")
    # elif user_password not in file:
    #     print("Ты ввёл не правильный Пароль")
