import time
import random
import pwinput

slider = "========================="
print("Привет, меня зовут. Крокодил")
time.sleep(2)
print("Играть с другом или ботом?")
time.sleep(2)
print("Игра с ботом:1 Игра с другом:2")
gamemod = input("1 или 2: ")
if gamemod == "1":
    wordlist = '''Кот Капуста Водитель Призидент'''.split()
    playagain = True
    while playagain:
        dbword = random.choice(wordlist)
        print("Бот загадывает слово")
        time.sleep(1)
        print(slider)
        time.sleep(1)
        print(slider)
        print("Бот приказал слово")
        time.sleep(1)
        print(slider)
        if dbword == "Кот":
            print("Подсказка")
            print(slider)
            print("Издает звуки мятов и стен")
            print(slider)
        elif dbword == "Капуста":
            print("Подсказка")
            print(slider)
            print("Зеленое растение-овощ из него берут детей")
            print(slider)
        elif dbword == "Водитель":
            print("Подсказка")
            print(slider)
            print("Управляет авто")
            print(slider)
        elif dbword == "Президент":
            print("Подсказка")
            print(slider)
            print("Высшая посда")
            print(slider)
        print("Введи слово:")
        bdword = input("")
        if bdword == dbword:
            print("Поздравляем вы угадали слово")
            print("Сыграть еще?")
            playagainss = input("y или n")
        elif bdword != dbword:
            print("Ошибка! вы не угадали слово")
            if dbword == "Кот":
                print("Подсказка")
                print(slider)
                print("Четыре лапе создания")
                print(slider)
            elif dbword == "Капуста":
                print("Подсказка")
                print(slider)
                print("Овощ листьями которого заворачивают голубцы")
                print(slider)
            elif dbword == "Водитель":
                print("Подсказка")
                print(slider)
                print("Возит людей")
                print(slider)
            elif dbword == "Президент":
                print("Подсказка")
                print(slider)
                print("За него голосую раз в 5 лет")
                print(slider)
            print("Еще раз введи слово")
            bdword = input("")
            if bdword == dbword:
                print("Поздравляем вы угадали слово")
            elif bdword != dbword:
                print("Ошибка! вы не угадали слово. Вы проиграли")
                print("Сыграть еще?")
                playagainss = input("y или n")
        if playagainss == "n":
            playagain = False



elif gamemod == "2":
    player_1_name = input("Игрок номер: 1 Как вас зовут?: ")
    player_2_name = input("Игрок номер: 2 Как вас зовут?: ")
    print('Игрок 1 загадывает слово')
    word = pwinput.pwinput(prompt="Введи слово: ", mask='*')
    oooo = input('Начинаем?')
    time.sleep(2)
    print(slider)
    print('Игрок 2 взирает слово')
    playagain = True
    while playagain:
        print("Игрок угадывает слово")
        sword = input("Введи слово:")
        if sword == word :
           print('Привет. Игрок 2 угадал слово')
           time.sleep(2)
           print("Еще раз?")
           playagains = input("y или n:")
           if playagains == "y":
               print("Игрок Загадывает слово")
               word = pwinput.pwinput(prompt="Введи слово новое слово: ", mask='*')
           elif playagains == "n":
                print("Спасибо за игру")
                playagain = False

        elif sword != word :
            print('ошибка. Игрок 2 не угадал слово')
            print('Грец 1 подсказывает')
            hel = input("Введи подсказку:")
            print(hel)