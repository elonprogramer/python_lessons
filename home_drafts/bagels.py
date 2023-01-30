import random

max_input = 3

letters = "1234567890"
# letters = list(letters)
# lenlist = len(letters)
letters_choice = ""
while len(letters_choice) != 3:
    letters_choice += random.choice(letters)

# print(letters_choice)
letters_choice_list = list(letters_choice)
# print(letters_choice_list)

print('Я загадаю %s-х значное число, которое вы должны отгадать.' % (max_input))
print('Я дам несколько подсказок...')
print('Когда я говорю:Это означает:')
print(' Холодно Ни одна цифра не отгадана.')
print(' Тепло Одна цифра отгадана, но не отгадана ее позиция.')
print(' Горячо Одна цифра и ее позиция отгаданы.')

MAX_GUESS = 5
game_guess = 5
game_true = True
print(f'Итак, я загадал число. У вас есть  попыток, чтобы отгадать его. {MAX_GUESS}')

while game_true:
    game_guess = game_guess - 1
    user_input = input("Введи 3 Цыфри:")

    user_input_answer = list(user_input)
    user_input_length = len(user_input)

    if user_input_length > max_input:
        print("Ты ввел больше цыфр")
    elif user_input_length < max_input:
        print("Ты ввел меньше цыфр")

    elif user_input_length == max_input:
        if user_input_answer == letters_choice_list:
            print("Гарячо")
            print("Игра вииграна")
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
