# works
import time
import os

tic = "0"
tac = "X"
grafix = """
*--------------*
    7 | 8 | 9
    --+-+--
    4 | 5 | 6
    --+-+--
    1 | 2 | 3
*--------------*
"""

def start():
    print("Привет! Игра крестики нолики начинается")
    print("#" * 20)
    time.sleep(1)
    os.system('clear')

    user_game_mode = input("Нолик = 1 Крестик = 2: ")
    if user_game_mode == '1':
        user_game_mode = 1
    elif user_game_mode == '2':
        user_game_mode = 2
    else:
        print("Введена ошибка")

    return user_game_mode


def show_victory(f):
    if f == tac:
        winner_name = 'Хрестик'
    else:
        winner_name = 'Нолик'
    os.system('clear')
    print(f"winner is {f} === {winner_name}")


def skip_your_turn(game_nums):
    game_nums = game_nums - 1
    print("Вы походили в занятую ячейку ¯\_(ツ)_/¯")
    print("Пропуск хода")
def game():
    game_nums = 0
    playing = True

    one = [' ', 'True']
    two = [' ', 'True']
    three = [' ', 'True']
    four = [' ', 'True']
    five = [' ', 'True']
    six = [' ', 'True']
    seven = [' ', 'True']
    eight = [' ', 'True']
    nine = [' ', 'True']

    user_game_mode = start()
    while playing:
        os.system('clear')
        grafix_func = f"""
*--------------*
    {seven[0]} | {eight[0]} | {nine[0]}
    --+-+--
    {four[0]} | {five[0]} | {six[0]}
    --+-+--
    {one[0]} | {two[0]} | {three[0]}
*--------------*
    """
        print(grafix)
        print(grafix_func)
        playing_second_cycle = True
        while playing_second_cycle:
            if user_game_mode == 1:  # нолик
                funk = tic
                print("Сейчас ходит нолик")
                time.sleep(0.4)
                print(f"Где поставить '{funk}'")
                game_input = int(input())
                user_game_mode = 2
            elif user_game_mode == 2: # крестик
                funk = tac
                print("Сейчас ходит крестик")
                time.sleep(0.4)
                print(f"Где поставить '{funk}'")
                game_input = int(input())
                user_game_mode = 1

            # обрабатываем ввод пользователя
            if game_input == 1:
                if one[1] == "True":
                    game_nums = game_nums + 1
                    one[0] = funk
                    one[1] = False
                # TODO: тут нужен else - вызываем функцию skip_your_turn(game_nums)
                else:
                    skip_your_turn(game_nums)
                playing_second_cycle = False
            elif game_input == 2:
                if two[1] == "True":
                    game_nums = game_nums + 1
                    two[0] = funk
                    two[1] = False
                else:
                    skip_your_turn(game_nums)
                playing_second_cycle = False
            elif game_input == 3:
                if three[1] == "True":
                    game_nums = game_nums + 1
                    three[0] = funk
                    three[1] = False
                else:
                    skip_your_turn(game_nums)
                playing_second_cycle = False
            elif game_input == 4:
                if four[1] == "True":
                    game_nums = game_nums + 1
                    four[0] = funk
                    four[1] = False
                else:
                    skip_your_turn(game_nums)
                playing_second_cycle = False
            elif game_input == 5:
                if five[1] == "True":
                    game_nums = game_nums + 1
                    five[0] = funk
                    five[1] = False
                else:
                    skip_your_turn(game_nums)
                playing_second_cycle = False
            elif game_input == 6:
                if six[1] == "True":
                    game_nums = game_nums + 1
                    six[0] = funk
                    six[1] = False
                else:
                    skip_your_turn(game_nums)
                playing_second_cycle = False
            elif game_input == 7:
                if seven[1] == "True":
                    game_nums = game_nums + 1
                    seven[0] = funk
                    seven[1] = False
                else:
                    skip_your_turn(game_nums)
                playing_second_cycle = False
            elif game_input == 8:
                if eight[1] == "True":
                    game_nums = game_nums + 1
                    eight[0] = funk
                    eight[1] = False
                else:
                    skip_your_turn(game_nums)
                playing_second_cycle = False
            elif game_input == 9:
                if nine[1] == "True":
                    game_nums = game_nums + 1
                    nine[0] = funk
                    nine[1] = False
                else:
                    skip_your_turn(game_nums)
                playing_second_cycle = False


        # ПРОВЕРКА ВЫИГРЫША

        if one[0] == funk:
            if two[0] == funk:
                if three[0] == funk:
                    #print(f"Ты выиграл")
                    show_victory(funk)
                    playing = False
            elif five[0] == funk:
                if nine[0] == funk:
                    #print("Ты выиграл2")
                    show_victory(funk)
                    playing = False
            elif four[0] == funk:
                if seven[0] == funk:
                    #print("Ты выиграл3")
                    show_victory(funk)
                    playing = False
        elif two[0] == funk:
            if five[0] == funk:
                if eight[0] == funk:
                    #print("Ты выиграл4")
                    show_victory(funk)
                    playing = False
        elif three[0] == funk:
            if six[0] == funk:
                if nine[0] == funk:
                    #print("Ты выиграл5")
                    show_victory(funk)
                    playing = False
            elif five[0] == funk:
                if seven[0] == funk:
                    #print("Ты выиграл6")
                    show_victory(funk)
                    playing = False
        elif four[0] == funk:
            if five[0] == funk:
                if six[0] == funk:
                    #print("Ты выиграл7")
                    show_victory(funk)
                    playing = False
        elif seven[0] == funk:
            if eight[0] == funk:
                if nine[0] == funk:
                    #print("Ты выиграл8")
                    show_victory(funk)
                    playing = False

        # Все клетки заняты - никто не выиграл
        if one[1] == False:
            if two[1] == False:
                if three[1] == False:
                    if four[1] == False:
                        if five[1] == False:
                            if six[1] == False:
                                if seven[1] == False:
                                    if eight[1] == False:
                                        if nine[1] == False:
                                            print("Ничья!")
                                            playing = False

        # os.system('clear')
        grafix_func = f"""
*--------------
    {seven[0]} | {eight[0]} | {nine[0]}
    --+-+--
    {four[0]} | {five[0]} | {six[0]}
    --+-+--
    {one[0]} | {two[0]} | {three[0]}
*--------------*
        """
        print(grafix_func)
        time.sleep(0.4)


def end_game():
    print("Игра окончена")
    print("\n\n")
    print("Желаете сыграть снова?")
    play_restart = int(input("Да = 1: "))
    if play_restart == 1:
        print("Играем!")
        return True
    else:
        print("Спасибо за игру, удачи!")
        return False


if __name__ == "__main__":
    main_game = True
    while main_game == True:
        game()
        # game_numbers()
        main_game = end_game()