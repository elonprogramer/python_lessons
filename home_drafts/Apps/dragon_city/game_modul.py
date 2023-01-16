import time
import mini_games
import moduls

def main_game(money):
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
        print(f"Money before game {money}")
        money = mini_games.money_game(money)
        print(f"Money after game {money}")
        moduls.data_write_money(money)
    elif game_mode == 1:
        mini_games.food_game(food) 
    elif game_mode == 2:
        mini_games.dragons_game(dragons)
def stats():
    user_id = 1
    


def main(money, dragons):
    print("Игра загружается")
    times = 3
    while times:
        print("################################")
        times = times -1
        if times == 0:
            times = False
    print("Здравствуйте! Вам предстоит поднять страну драконов ")
    time.sleep(2)
    print(f"ваша статистика: \n Деньги: {money} \n Количество драконов: {dragons}")


def get_user_data(user_id):
    #print(f"user_id: {user_id} {type(user_id)}")
    file_logins = open("./logins.txt", "r")
    user_logins_list = file_logins.read().splitlines()
    our_user_data = user_logins_list[int(user_id) - 1]
    #print(f'USER DATA = {our_user_data}')
    # 1 sasha 12345 1 51 1000 6

    user_id, name, password ,money, food, resource, dragons = our_user_data.split(' ')
    # print(f'ВАША СТАТИСТИКА: {money=} {food=} {resource=} {dragons=}')
    return user_id, name, password ,money, food, resource, dragons
    

def game_money():
    # TODO: Очищать консоль
    print("Вы вошли в режим зарабатывание денег!")
    print("Запуск игры...")
    playing_game = True
    while playing_game:
        pass
    

def game_food():
    pass


def game_dragons():
    pass