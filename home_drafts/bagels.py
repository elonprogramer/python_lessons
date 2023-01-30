import random

DEBUG_MODE = 1
MAX_INPUT = 3


def debug_print(str_in):
    if DEBUG_MODE == 1:
        print(str_in)

letters = "1234567890"
# letters = list(letters)
# lenlist = len(letters)
letters_choice = ""


while len(letters_choice) != 3:
    letters_choice += random.choice(letters)

letters_choice = "147"

debug_print(f'{letters_choice=}')
letters_choice_list = list(letters_choice)
# print(letters_choice_list)

print('Я загадаю %s-х значное число, которое вы должны отгадать.' % (MAX_INPUT))
print('Я дам несколько подсказок...')
print('Когда я говорю:Это означает:')
print(' Холодно Ни одна цифра не отгадана.')
print(' Тепло Одна цифра отгадана, но не отгадана ее позиция.')
print(' Горячо Одна цифра и ее позиция отгаданы.')

MAX_GUESS = 5
game_guess = 5
game_true = True
print(f'Итак, я загадал число. У вас есть {MAX_GUESS} попыток, чтобы отгадать его.')


while game_true:
    game_guess = game_guess - 1
    user_input = input("Введи 3 Цифры: ")

    user_input_answer = list(user_input)
    user_input_length = len(user_input)

    if user_input_length > MAX_INPUT:
        print("Ты ввел больше цифр")
    elif user_input_length < MAX_INPUT:
        print("Ты ввел меньше цифр")
    elif user_input_length == MAX_INPUT:
        if user_input_answer == letters_choice_list:
            print("Горячо")
            print("Игра выиграна")
            game_true = False
            game_guess = game_guess + 1

        elif user_input_answer != letters_choice_list:
            for i in letters_choice_list:
                if i in user_input_answer:
                    print(i)
                    # print('\n\n')
                    # print("тепло")
                else:
                    print("Холодно")

    if game_guess == 0:
        print("Игра проиграна")
        game_true = False
