import time

def start():
    print("Привет. в прошлой части ты обокрал страну драконов")
    time.sleep(1)
    print("Пока ты тратил свои деньги . Драконы подали в суд, и выиграли дело")
    time.sleep(1)
    print("Твое наказание - Востановить економику страны драконов!")
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
    id = 0
    id = id + 1
    user_data = str(f"id = {id} \n name = {user_login} \n password = {second_password}")
    file = open("/home/elon/python_lessons/home_drafts/Apps/dragon_city/config.txt", "a")
    file.write(user_data)
    file.close()

def login():
    user_login = input("Введи имя: ")
    user_password = str(input("Введи пароль: "))
    file = open("/home/elon/python_lessons/home_drafts/Apps/dragon_city/config.txt", "r")
    if user_login in file and user_password in file:
        print(f"Поздравляю, {user_login}, Ты успешно авторизован!")
    elif user_login not in file:
        print("Ты ввёл не правельный логин")
    elif user_password not in file:
        print("Ты ввёл не правельный Пароль")
