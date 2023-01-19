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
    print("Привет! Игра хрестики нолики начинаеться")
    print("################################")
    time.sleep(1)
    os.system('clear')
    user_game_mode = input("Нолик = 1 Хрестик = 2: ")
    if user_game_mode == '1':
        user_game_mode = 1
    elif user_game_mode == '2':
        user_game_mode = 2

    else:
        print("Введина ошыбка")
    return user_game_mode

one = [' ', 'True']
two = [' ', 'True']
three = [' ', 'True']
four = [' ', 'True']
five = [' ', 'True']
six = [' ', 'True']
seven = [' ', 'True']
eight = [' ', 'True']
nine = [' ', 'True']



def game():
    plaing = True

    user_game_mode = start()
    while plaing:
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
        plaings = True
        while plaings:
            if user_game_mode == 1:
                funk = tic
                print("Сейчас ходит нолик")
                time.sleep(1)
                print(f"Где поставить '{funk}'")
                game_input = int(input())
                user_game_mode = 2
            elif user_game_mode == 2:
                funk = tac
                print("Сейчас ходит крестик")
                time.sleep(1)
                print(f"Где поставить '{funk}'")
                game_input = int(input())
                user_game_mode = 1
            if game_input == 1:
                if one[1] == "True":
                    one[0] = funk
                    one[1] = False
                plaings = False
            elif game_input == 2:
                if two[1] == "True":
                    two[0] = funk
                    two[1] = False
                plaings = False
            elif game_input == 3:
                if three[1] == "True":
                    three[0] = funk
                    three[1] = False
                plaings = False
            elif game_input == 4:
                if four[1] == "True":
                    four[0] = funk
                    four[1] = False
                plaings = False
            elif game_input == 5:
                if five[1] == "True":
                    five[0] = funk
                    five[1] = False
                plaings = False
            elif game_input == 6:
                if six[1] == "True":
                    six[0] = funk
                    six[1] = False
                plaings = False
            elif game_input == 7:
                if seven[1] == "True":
                    seven[0] = funk
                    seven[1] = False
                plaings = False
            elif game_input == 8:
                if eight[1] == "True":
                    eight[0] = funk
                    eight[1] = False
                plaings = False
            elif game_input == 9:
                if nine[1] == "True":
                    nine[0] = funk
                    nine[1] = False
                plaings = False


        if one[0] == funk:
            if two[0] == funk:
                if three[0] == funk:
                    print("Ты выиграл")
                    plaing = False
                    plaings = False
            elif four[0] == funk:
                if seven[0] == funk:
                    print("Ты выиграл")
                    plaing = False
                    plaings = False
        elif two[0] == funk:
            if five[0] == funk:
                if eight[0] == funk:
                    print("Ты выиграл")
                    plaing = False
                    plaings = False
        elif three[0] == funk:
            if six[0] == funk:
                if nine[0] == funk:
                    print("Ты выиграл")
                    plaing = False
                    plaings = False
        elif four[0] == funk:
            if five[0] == funk:
                if six[0] == funk:
                    print("Ты выиграл")
                    plaing = False
                    plaings = False
        elif seven[0] == funk:
            if eight[0] == funk:
                if nine[0] == funk:
                    print("Ты выиграл")
                    plaing = False
                    plaings = False
        if nine[0] == funk:
            if five[0] == funk:
                if one[0] == funk:
                    print("Ты выиграл")
                    plaing = False
                    plaings = False
        elif seven[0] == funk:
            if five[0] == funk:
                if three[0] == funk:
                    print("Ты выиграл")
                    plaing = False
                    plaings = False


        if one[1] == False:
            if two[1] == False:
                if three[1] == False:
                    if four[1] == False:
                        if five[1] == False:
                            if six[1] == False:
                                if seven[1] == False:
                                    if eight[1] == False:
                                        if nine[1] == False:
                                            print("Проиграш")
                                            plaing = False
                                            plaings = False
def end_game():
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
    print(grafix_func)
    time.sleep(2)
    print("Вы выиграли!!!")
    print("\n\n\n\n\n\n\n\n\n\n")
    print("Желаете сыграть снова?")
    play_restart = int(input("Да = 1: "))
    if play_restart == 1:
        game()
    else:
        print("Спасибо за игру, удачи!")



game()
end_game()