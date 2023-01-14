import game_modul
import time
import mini_games


def main_game_menu(user_id):
    print(f'к нам пришел игрок под номером {user_id}')

    user_id, name, password, money, food, resource, dragons = game_modul.get_user_data(user_id)

    print(f'у игрока {user_id}: данные: {money=} {food=} {resource=} {dragons=}')
    dragons_family = int(dragons) / 2


    playings = True
    while playings:
        print("Выбери работу на сегодня:")
        time.sleep(2)
        work_list = "Деньги Еду Драконов"
        work_lists = work_list.split()
        for i in work_lists:
            list_index = work_lists.index(i)
            print(f"Добывать {i} = {list_index}")
        print("")
        game_mode = int(input("Номер режима: "))
        if game_mode == 0:
            mini_games.money_game(money) # TODO money_game должна возвращать новое значение money
        elif game_mode == 1:
            mini_games.food_game(food) 
        elif game_mode == 2:
            mini_games.dragons_game(dragons)

        # TODO написать функцию которая будет
        # открывать файлик logins.txt считывать оттуда все данные в массив
        # менять строчку с нашим пользователем на новые данные - те что стали после игр

if __name__ == "__main__":
    main_game_menu(1)