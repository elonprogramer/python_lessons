import random
import time

health = 2
win = False
money = 0
right_door = random.randint(1, 4)  # номер правильной двери
print(f"RIGHT DOOR:{right_door}")
print("Привет. Ты попал в пещеру с сокровищами!!!!")
time.sleep(1)
time.sleep(1)
print("Теперь тебе надо сбежать от семьи драконов")
time.sleep(1)
print(f"Перед тобой 4 двери и у {health} жизней")

playing = True
print("Привет. Выбери игру")
print("Уможать or Добавлять")
game_type = input()
if  game_type in ('Умножать','Множить','умножать','множить','m') :
    while playing:
        # right_door - номер двери где сидит главный дракон
        door = int(input("Выбери дверь от 1 до 4: "))
        if door == right_door:
            print('Поздравляю ты угадал дверь')
            print("Смотри!!! Здесь есть сундук!")
            print("Открыть сундук?")
            sunduk_answer = input()
            if sunduk_answer in ('Да', 'да', 'yes', 'y', 'si', 'так', 'tak'):
                print("Ой тут пароль...")
                time.sleep(2)
    
                num1 = random.randint(3, 9)
                num2 = random.randint(3, 9)
    
                print(f"Подсказка: это {num1} yмножить на {num2}")
                pass_user_input = int(input("Введи ответ: "))
                right_pass = num1 * num2
    
                if pass_user_input == right_pass:
                    print("Молодец ты нашел золотое яблоко")
                    health = health + 2
                    print(f"Твое здоровье увеличилось и равняется: {health}")
                else:
                    print(f'ты не угадал пароль был {right_pass}')
    
            print("Вот и золотые ворота")
            time.sleep(1)
    
            print("О нет!!!")
            time.sleep(1)
    
            print("Перед тобой главный дракон")
            print(f"У тебя осталось {health} жизней. Тебе прeдстоит убить главного дракона чтобы выжить и сохранить сокровища!")
            time.sleep(1)
    
            while health > 0:
                num1 = random.randint(5, 9)
                num2 = random.randint(5, 9)
                print(f"Дракон спрашивает сколько будет если {num1} умножить на {num2}?")
                right_answer = num1 * num2
                time.sleep(2)
                user_answer = input("Введите ответ: ")
                if int(user_answer) == int(right_answer):
                    money = money + 1000
                    print("Ты убил главного дракона")
                    print("и ты выиграл  игру!!!!")
                    playing = False
                    win = True
                    break
                else:
                    health = health - 1
                    print(f"Вас укусил дракон, вы потеляли жизнь у вас осталось {health} жизней")
    
            playing = False
        else:
            # пользователь не угадал дверь и попал к маленькому дракону
            # делаем так чтобы пользователь мог ответить на вопрос дракона и не потерять жизнь и получить деньги
            print('вы наткнулись на маленького дракона, ответь на его вопрос чтобы не потерять жизни')
            n1 = random.randint(3, 5)
            n2 = random.randint(3, 5)
            print(f"Сколько будет {n1} yмножить на {n2}?")
            pass_user_input = int(input("Введи ответ: "))
            right_answer = n1 * n2
    
            if int(pass_user_input) == int(right_answer):
                # мы убили дракона
                money = money + 100
                print(f"вы угадали и убили дракона, теперь у вас {health} жизней и {money} денег")
            else:
                health = health - 1
                print(f"вы не угадали, вас укусил дракон, у вас осталось {health} жизней")
    
            if health == 0:
                print("ты проиграл")
                playing = False


elif game_type in ('Добавлять','добавлять','Складывать','складывать','d',):
    while playing:
        # right_door - номер двери где сидит главный дракон
        door = int(input("Выбери дверь от 1 до 4: "))
        if door == right_door:
            print('Поздравляю ты угадал дверь')
            print("Смотри!!! Здесь есть сундук!")
            print("Открыть сундук?")
            sunduk_answer = input()
            if sunduk_answer in ('Да', 'да', 'yes', 'y', 'si', 'так', 'tak'):
                print("Ой тут пароль...")
                time.sleep(2)
    
                num1 = random.randint(10, 100)
                num2 = random.randint(1, 10)
    
                print(f"Подсказка: это {num1} +  {num2}")
                pass_user_input = int(input("Введи ответ: "))
                right_pass = num1 + num2
    
                if pass_user_input == right_pass:
                    print("Молодец ты нашел золотое яблоко")
                    health = health + 2
                    print(f"Твое здоровье увеличилось и равняется: {health}")
                else:
                    print(f'ты не угадал пароль был {right_pass}')
    
            print("Вот и золотые ворота")
            time.sleep(1)
    
            print("О нет!!!")
            time.sleep(1)
    
            print("Перед тобой главный дракон")
            print(f"У тебя осталось {health} жизней. Тебе прeдстоит убить главного дракона чтобы выжить и сохранить сокровища!")
            time.sleep(1)
    
            while health > 0:
                num1 = random.randint(10, 100)
                num2 = random.randint(10, 100)
                print(f"Дракон спрашивает сколько будет если {num1} +  {num2}?")
                right_answer = num1 + num2
                time.sleep(2)
                user_answer = input("Введите ответ: ")
                if int(user_answer) == int(right_answer):
                    money = money + 1000
                    print("Ты убил главного дракона")
                    print("и ты выиграл  игру!!!!")
                    playing = False
                    win = True
                    break
                else:
                    health = health - 1
                    print(f"Вас укусил дракон, вы потеляли жизнь у вас осталось {health} жизней")
    
            playing = False
        else:
            # пользователь не угадал дверь и попал к маленькому дракону
            # делаем так чтобы пользователь мог ответить на вопрос дракона и не потерять жизнь и получить деньги
            print('вы наткнулись на маленького дракона, ответь на его вопрос чтобы не потерять жизни')
            n1 = random.randint(3, 5)
            n2 = random.randint(3, 5)
            print(f"Сколько будет {n1} yмножить на {n2}?")
            pass_user_input = int(input("Введи ответ: "))
            right_answer = n1 * n2
    
            if int(pass_user_input) == int(right_answer):
                # мы убили дракона
                money = money + 100
                print(f"вы угадали и убили дракона, теперь у вас {health} жизней и {money} денег")
            else:
                health = health - 1
                print(f"вы не угадали, вас укусил дракон, у вас осталось {health} жизней")
    
            if health == 0:
                print("ты проиграл")
                playing = False

    
if win:
    print("Поздравляем ты выиграл")
else:
    print("Ты проиграл, попробуй еще раз")
