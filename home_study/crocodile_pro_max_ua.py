import time
import random
import pwinput

slider = "========================="
print("Привіт, мене звати. Крокодил")
time.sleep(2)
print("Грати з другом чи ботом?")
time.sleep(2)
print("Гра з ботом:1 Гра з другом:2")
gamemod = input("1 or 2: ")
if gamemod == "1": 
    wordlist = '''Кіт Капуста Водій Призидент'''.split()
    playagain = True
    while playagain:
        dbword = random.choice(wordlist)
        print("Бот загадує слово")
        time.sleep(1)
        print(slider)
        time.sleep(1)
        print(slider)
        print("Бот загадав слово")
        time.sleep(1)
        print(slider)
        if dbword == "Кіт":
            print("Підказка")
            print(slider)
            print("Видає звуки м'яв та мур")
            print(slider)    
        elif dbword == "Капуста":
            print("Підказка")
            print(slider)
            print("Зелена рослина-овоч з неї беруть дітей")
            print(slider)   
        elif dbword == "Водій":
            print("Підказка")
            print(slider)
            print("Керує авто")
            print(slider)   
        elif dbword == "Призидент":
            print("Підказка")
            print(slider)
            print("Найвища посда")
            print(slider)
        print("Введи слово:")
        bdword = input("")
        if bdword == dbword:
            print("Вітаємо ви вгадали слово")
            print("Зіграти ще?")
            playagainss = input("y or n")
        elif bdword != dbword:
            print("Помилка! ви не вгадали слово")
            if dbword == "Кіт":
                print("Підказка")
                print(slider)
                print("Чотири лапе створіння")
                print(slider)    
            elif dbword == "Капуста":
                print("Підказка")
                print(slider)
                print("Овоч листям якого загортають голубці")
                print(slider)   
            elif dbword == "Водій":
                print("Підказка")
                print(slider)
                print("Возить людей")
                print(slider)   
            elif dbword == "Призидент":
                print("Підказка")
                print(slider)
                print("За нього голосую раз у 5 років")
                print(slider)
            print("Ще раз введи слово")
            bdword = input("")
            if bdword == dbword:
                print("Вітаємо ви вгадали слово")
            elif bdword != dbword:
                print("Помилка! ви не вгадали слово. Ви програли")
                print("Зіграти ще?")
                playagainss = input("y or n")
        if playagainss == "n":
            playagain = False



elif gamemod == "2":
    player_1_name = input("Гравець номер: 1 Як вас звати?: ")
    player_2_name = input("Гравець номер: 2 Як вас звати?: ")
    print('Гравець 1 загадує слово')
    word = pwinput.pwinput(prompt="Введи слово: ", mask='*')
    oooo = input('Починаємо?')
    time.sleep(2)
    print(slider)
    print('Гравець 2 вгдує слово')
    playagain = True
    while playagain:
        print("Гравець вгадує слово")
        sword = input("Введи слово: ")
        if sword == word :
           print('Вітаю. Гравець 2 вгадав слово')
           time.sleep(2)
           print("Ще раз?")
           playagains = input("y or n: ")
           if playagains == "y":
               print("Гравець Загадує слово")
               word = pwinput.pwinput(prompt="Введи слово нове слово: ", mask='*') 
           elif playagains == "n":
                print("Дякую за гру")
                playagain = False

        elif sword != word :
            print('помилка. Гравець 2 не вгадав слово')
            print('Грвець 1 дає підказку')
            hel = input("Введи підказку: ")
            print(hel)
