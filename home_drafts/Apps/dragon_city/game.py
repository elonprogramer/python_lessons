import game_modul
import time
import mini_games
import moduls

def main_game_menu(user_id):
    #print(f'к нам пришел игрок под номером {user_id}')

    user_id, name, password, money, food, resource, dragons = game_modul.get_user_data(user_id)

    #print(f'у игрока {user_id}: данные: {money=} {food=} {resource=} {dragons=}')
    dragons_family = int(dragons) / 2


    playings = True
    while playings:
        moduls.main_menu()    

        # TODO написать функцию которая будет
        # открывать файлик logins.txt считывать оттуда все данные в массив
        # менять строчку с нашим пользователем на новые данные - те что стали после игр

if __name__ == "__main__":
    main_game_menu(1)