import random

def money_game(money):
    playing_game = True
    while playing_game:
        num1 = random.randint(6, 9)
        num2 = random.randint(6, 9)
        print(f"Сколько будет {num1} Умножить на {num2}")
        user_answer = input()
        right_answer = num1*num2
        if user_answer == right_answer:
            print("Правильно!")
            money = money + 10
        else:
            print("Ошибка")


def food_game(food):
    playing_game = True
    while playing_game:
        num1 = random.randint(1, 10)
        num2 = random.randint(2, 10)
        print(f"Сколько будет {num1} Умножить на {num2}")
        user_answer = input()
        right_answer = num1*num2
        if user_answer == right_answer:
            print("Правильно!")
            food = food + 5
        else:
            print("Ошибка")

def dragons_game(dragons):
    playing_game = True
    while playing_game:
        num1 = random.randint(1, 10)
        num2 = random.randint(2, 10)
        print(f"Сколько будет {num1} Умножить на {num2}")
        user_answer = input()
        right_answer = num1*num2
        if user_answer == right_answer:
            print("Правильно!")
            food = dragons + 5
        else:
            print("Ошибка")
