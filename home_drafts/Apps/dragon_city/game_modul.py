import time
import mini_games

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

    file_logins = open("./logins.txt", "r")
    user_logins_list = file_logins.read().splitlines()
    our_user_data = user_logins_list[user_id - 1]
    print(f'USER DATA = {our_user_data}')
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