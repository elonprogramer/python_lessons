import time
import random
import pwinput
slider = "========================="
print("Привіт, мене звати. Крокодил")
time.sleep(2)
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
    sword = input("Введи слово: ")
    if sword == word :
        print('Вітаю. Гравець 2 вгадав слово')
        time.sleep(2)
        print("Ще раз?")
        playagains = input("y or n: ")
        if playagains == "y":
           word = pwinput.pwinput(prompt="Введи слово нове слово: ", mask='*') 
        elif playagains == "n":
            print("Дякую за гру")
            playagain = False

    elif sword != word :
        print('помилка. Гравець 2 не вгадав слово')
        print('Грвець 1 дає підказку')
        hel = input("Введи підказку: ")
        print(hel)
