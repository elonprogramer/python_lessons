import time
import mini_games

def main(money, dragons):
    print("Игра загружаеться")
    times = 3
    while times:
        print("################################")
        times = times -1
        if times == 0:
            times = False
    print("Здраствуйте! Вам притсоит поднять страну драконов ")
    time.sleep(2)
    print(f"ваша статистика: \n Денги: {money} \n Количество драконов: {dragons}")


def game(money, food, resource, dragons,  dragons_family):
    money = money
    food = food
    resource = resource
    dragons = dragons
    dragons_family = dragons_family
    

def game_money():
    # TODO: Очищать консоль
    print("Вы вошли в режим заробатывание дениг!")
    print("Запуск игры...")
    playing_game = True
    while playing_game:
        pass
    

def game_food():
    pass


def game_dragons():
    pass