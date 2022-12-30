import game_modul
import time
import mini_games

money = 0
food = 50
resource = 100
dragons = 6
dragons_family = dragons / 2

game_modul.main(money, dragons)

game_modul.game(money, food, resource, dragons,  dragons_family)
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
    game_mode = input("Номер режыма: ")
    if game_mode == 0:
        mini_games.money_game(money)
    elif game_mode == 1:
        pass
    elif game_mode == 2:
        pass