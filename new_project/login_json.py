import json


def read_json():
    try:
        data = json.load(open("./persons.json", "r"))
    except:
        data = {}

    # print(f"data = {type(data)}: {data}")
    return data


def last_user_id():
    try:
        data = read_json()
        last_id = sorted(data.keys())[-1]
        last_id = int(last_id)
        last_id = last_id + 1
    except AttributeError:
        last_id = 0
        # print(last_id)
    except IndexError:
        last_id = 0
    except:
        last_id = 0
    return last_id


def login():
    data = read_json()
    person_login_dict = {}
    person_password_dict = {}
    print("Введите Логин")
    user_login = input("Login: ")
    print("Введи пароль")
    user_password = input("Password: ")
    for name_key in data.keys():
        # print(f'{name_key=}')
        person_login_dict[data[name_key]['login']] = name_key
        person_password_dict[data[name_key]['password']] = name_key
        if user_login in person_login_dict:
            key_id = person_login_dict[user_login]
            if user_password in person_password_dict:
                print(f"Login = {data[key_id]['login']} \nPassword = {data[key_id]['password']}")
            else:
                print("Пользователь не существует в базе данных")
        else:
            print("Пользователь не существует в базе данных")


def signup():
    last_id = last_user_id()
    try:
        data = json.load(open("./persons.json"))
        # print(f"data = {type(data)}: {data}")
    except:
        data = {}
    
    print("Введите логин")
    user_login = input("Login: ")
    print("Введите пароль: ")
    user_password = input("Password: ")
    pass_true = True
    while pass_true:
        user_password_next = input("Password: ")
        if user_password != user_password_next:
            print("Пароли не совпадают")
        elif user_password == user_password_next:
            pass_true = False

    data[last_id] = {
        "login": user_login,
        "password": user_password_next,
    }
    # print(f"RES: {type(data)} data ={data}")
    # print(f"data = {type(data)}: {data}")
    # print("we are here 1")

    with open("./persons.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def main():
    print("Зарегистрироваться = 1 Войти = 2")
    user_input = int(input("1 or 2"))
    if user_input == 1:
        signup()
    elif user_input == 2:
        login()


if __name__ == "__main__":
    main()
