import moduls
moduls.start()  # Приветствие игрока
print("Войти = 1 Зарегистрироваться = 2 Гость = 3")
game_mode = int(input())
if game_mode == 1:
    moduls.login()
elif game_mode == 2:
    moduls.signup()
elif game_mode == 3:
    print("В разработке")
    print("Хотите зарегистрироваться? что-бы сыграть")
    user_game_input = input("y or n")
    if user_game_input == "y" or user_game_input == "д":
        moduls.sigin()
    else:
        print("Ошибка")
else:
    print("Ошибка")
