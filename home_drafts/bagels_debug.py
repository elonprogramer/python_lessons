import random
import sys

DEBUG_MODE = 1


print(f"cкрипт : {sys.argv[0]} - это игра в числа")

def debug_print(str_in):
    if DEBUG_MODE == 1:
        print(str_in)


def random_choice(number_size):
    letters = "123456789"
    # letters = list(letters)
    # lenlist = len(letters)
    letters_choice = ""
    while len(letters_choice) != int(number_size):
        random_num = random.choice(letters)
        if random_num not in letters_choice:
            letters_choice += random_num
    return letters_choice


def main():
    print('MAIN')
    a1 = sys.argv[1]
    MAX_INPUT = int(a1)
    print(f'first_param  = {a1}')
    # a2 = sys.argv[2]

    # letters_choice = "147"
    letters_choice = random_choice(a1)

    debug_print(f'{letters_choice=}')

    letters_choice_list = list(letters_choice)
    debug_print(letters_choice_list)

    print('Я загадаю %s-х значное число, которое вы должны отгадать.' % (MAX_INPUT))
    print("\n\n\n\n")
    print('Я дам несколько подсказок...')
    print('Когда я говорю:Это означает:')
    print(' Тепло если цифра отгадана')
    print(' Горячо если все цифры отгаданы')


    MAX_GUESS = 10
    game_guess = 5
    game_true = True
    print(f'Итак, я загадал число. У вас есть {MAX_GUESS} попыток, чтобы отгадать его.')

    while game_true:
        game_guess = game_guess - 1
        user_input = input(f"Введи {MAX_INPUT} Цифры: ")

        user_input_answer = list(user_input)
        user_input_length = len(user_input)

        if user_input_length > MAX_INPUT:
            print("Ты ввел больше цифр")
        elif user_input_length < MAX_INPUT:
            print("Ты ввел меньше цифр")
        elif user_input_length == MAX_INPUT:
            if set(user_input_answer) == set(letters_choice_list):   # ['1', '2', '3'] == ['1', '3', '2']
                print("Горячо")
                print("Игра выиграна")
                game_true = False
                game_guess = game_guess + 1

            else:
                for i in letters_choice_list:
                    if i in user_input_answer:
                        print("Тепло", end=" ")
                        print("\n")
                    else:
                        pass



if __name__ == '__main__':
    main()
    fail_flag = 0

    '''
    Тестируем генерацию числа:
    
    for i in range(1000):
        # print(f'запускаем {i} - проверку функции генерации числа')
        number_for_check = random_choice()
        print(type(number_for_check))
        # print(f'{number_for_check=}')
        if len(set(list(number_for_check))) != 3:
            # print("BAD case")
            fail_flag = 1
        else:
            # print("good case")
            pass

    if fail_flag == 1:
        print("BAD case")
    else:
        print("good case")
    '''


    # if set(letters_choice) != 3:
    #     debug_print(letters_choice)
    #     del letters_choice
    # else:
    #     letters_choice = letters_choice