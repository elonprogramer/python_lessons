import moduls
from game import main_game_menu

moduls.start()  # Приветствие игрока

print("Войти = 1 Зарегистрироваться = 2")
game_mode = int(input())
if game_mode == 1:
    user_id = moduls.login()
elif game_mode == 2:
    moduls.signup()
    print("Совершити вход:")
    user_id = moduls.login()
else:
    print("Ошибка")


if user_id:
    print('GAME START')
    user_id = 1
    main_game_menu(user_id)
else:
    print('goodbye')
