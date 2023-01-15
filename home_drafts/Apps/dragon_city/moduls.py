import time
import game_modul

def start():
    print("Привет.В прошлой части ты обокрал страну драконов")
    time.sleep(1)
    print("Пока ты тратил свои деньги, драконы подали в суд и выиграли дело")
    time.sleep(1)
    print("Твое наказание - Восcтановить экономику страны драконов!")

def main_menu():
    menu_grafix = """
    |*****************|    
    |   Мини-игры(1)  |
    |   Статистика(2) |  
    |   Выход(3)      |
    |*****************|
    """
    print(menu_grafix)
    menu_input = int(input("1 or 2 or 3"))
    if menu_input == 1:
        game_modul.main_game()
    elif menu_input == 2:
        game_modul.stats()



def last_user_id():
    file_last_id = open("./logins.txt", "r")
    user_id_lines = file_last_id.read().splitlines()
    user_last_id = len(user_id_lines)
    return user_last_id

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
    file_signup = open("./logins.txt", "r")
    user_id = last_user_id()
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
    login_user_id_dict = {}

    user_logins_list = file_logins.read().splitlines()
    for line in user_logins_list:
        #print(f'---{line}---')
        fields = line.split(' ')
        #print(f'name = {fields[1]}')
        login_pass_dict[fields[1]] = fields[2]
        login_user_id_dict[fields[1]] = fields[0]

    #print(login_pass_dict)

    if user_login in login_pass_dict.keys():
        user_id = login_user_id_dict[user_login]
        #print(f"WE HAVE USER {user_id} with name {user_login}")
        #print(f'WE HAVE USER {user_login}')
        if user_password == login_pass_dict[user_login]:
            print(f'Авторизация прошла успешно {user_login}')
        else:
            print('Пароль неверный')

    else:
        print(f'NO SUCH USER {user_login}')
    return user_id
    # if user_login in file and user_password in file:
    #     print(f"Поздравляю, {user_login}, Ты успешно авторизован!")
    # elif user_login not in file:
    #     print("Ты ввёл не правильный логин")
    # elif user_password not in file:
    #     print("Ты ввёл не правильный Пароль")

def data_write_money(user_id, money):
    file_read = open("./logins.txt", "r")
    lines = file_read.read().splitlines()
    new_lines = []
    for line in lines:
        print(line)
        user_fields = line.split(" ")
        print(user_fields[0])
        if user_fields[0] == str(user_id):
            print("found our user")
            print(user_fields)
            user_fields[3] = str(money)
        new_line = ' '.join(user_fields)
        new_lines.append(new_line)
    
    print(f"new lines {new_lines}") 
    file_read.close()
    file_write = open("./logins.txt", "w")
    new_file_content = '\n'.join(new_lines) + "\n"
    file_write.write(str(new_file_content))

def main_stats(user_id):

    user_id, name, password, money, food, resource, dragons = game_modul.get_user_data(user_id)

    print(f'Данные: {money=} {food=} {resource=} {dragons=}')
    




if __name__ == "__main__":
    print("Starting data_write_money")