import random
import time
health = 5
money = 1000
sword = False
doortrue = random.randint(1,4)
print ("Привет. Ты угадал пищеру с сокровищами!!!!")
time.sleep(5)
num1 = random.randint(1,10)
num2 = random.randint(1,10)
print ("""
 ...... .. ......... .. ......... ............ ............ ............ ......... .. ......... .. .
................................::..................................................................
.............................:^^~!~^^:..............................................................
............................!~~^^~!~:~:.............................................................
............................:7~~^::!^^~.............................................................
............................ ^7^~^::~:~^.............:^^^:::::......................................
............................. !7^~^^^^^^^.. ........:^^^^^^:^.......................................
...........:.::.::............:^:^^^^^^^~~~!!77??JJYYY55YJY:^::.....................................
........:^!~:^^^^^^^^~~!!777??JJYYY5555PPPPPPPPPPPP55PYYJJY~:^......................................
.......:!77!:~:7555PPPPPPPGPPPPPP5555555555555555555PYYYYYJ7.:......................................
......::7?7!:~^!P555555555555555555555555555555555Y55YYYYYJJ::......................................
....:^^~7??7!~^^Y5555555555555555YYY555555Y555555YY555YYYYJY~:......................................
....^^!!7JJ?~~:^?5YYYYYYYYYYYYYYYYYYYYYYYY5555YYYYY555YYYYYY?::.....................................
...^^!7!??J?!!:^!YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYJJJJ5P55YY55YY::.....................................
...^~7!7??J?!!^^~YYYYYYYYYYYYYYJJJJYYJJJJJJJJJ???J?JP5555Y5YY!:.....................................
...~!?~7??JJ7!~^^?YJJJJJJJJJJJJ??????????????J?JJJJJ5P555Y555?::....................................
...~!?!!?JJY?7~^^!?????????????????JJJJJJJJ??????7777Y5P55555Y^:....................................
...^!?7~?JJ5J77~^~?J??JJJJJJJJJJ????7777777777777777??JPPP5555!^^...................................
....~7J7~?Y5Y?7!^~????77777777777777777???????JJ??J?????J55PPPJ:~::.................................
....:!?J7~7Y5J??!~!7777????????JJJJ????7!!!77!!!^^!!~~!7777??7!^~~^.................................
......~?JJ!!??7?7~!??????????????????77?7~^^^^:^!^:7!~^^^~~^^:^~^^^^:...............................
.......^7JJJ?!~::~~7????????JJ???7~!!~^^~~77!~!7!!7JJJ7~~^~~~~~^^:~~^^^: ...........................
.........~7JYJ?~:^~!7777!7~~~~^~~!!^^^7^^~!7~:^^~7!!?J!~?7^^^:~!!!!!~^^^^...........................
...........:~7??^~!~~~~~~!7!~~~!!~~!!!?7!~^^7~!!7~^::!7!!77!!!!7!~~7?7!!!~^::.......................
.............  ~?~^^^~!7^^^^^????~~!~^^77!^:7^~^^~^~?7~~^^7!^~~?J7~^^^~~~^~~^^:::...................
...............~J?!~^!!!777?7~7!~~~^^~~~~~!77^^^~!!!~!~~!~~7:^^!J?J7!!YY77?7^~~!!^:.................
...............~JJ?!!?J?7!~!777J7~^^7?7!!?7~^^:!!^^7~^^^^^^?7!~!^~~~!7!!^~7~^^~~^^^~~^^:............
................~YJ??YYJ???7!~~7?JJ!~~~~^^!7!77!^^:!Y7777?7~!!!?!~^^^^^^^!?!^^^^77?YJ7~^^::^^:......
............... ^?YJ?555YJJ???7~^~?!~!!~~~?775!~~!!~~~!!7!~^^~?7!77!!!77!!?J!!!!777!!~^^^^:::^:::...
................^7J?7555YY?~:^!77!~!!~777~~~!??7!7?!~^:^^~^^~~!^:^!777777!!~::::::^^^^~!J!:::.......
................^!?7?5555Y?7!^~???7!~~^~7!~^::^^7?7?7777!!~!!!!~!!^^^^^^^::::::::^^^~!7?!~!~~:::....
................^!?7JPJ???YY?7J~Y5J??7!~^!!!!!!!?!!!^^~~~~~~~!7!^^^^^^^::..~~~~!!77???Y?7?7!~::.....
................^!77Y?7PP55YY5J^5PYYYJ?7~^^^^^^^:::~??????777JJ^^^^!7!^^::~JJJJJJJJJJJY!~~^:........
................~!77Y??PGP5555Y~JP5YYJJ?7!~::::....~JJJJJJJJ55!~!!~~?Y^!!^~7J????????Y~:::..........
..............:^:!??5PJ?Y5P5555J^Y5YYYJ??7!^~^^:::^JYYYJJYYJ5J~!!^^~??~77?!:^?JJJJJJY!^^^...........
..............^J!~!!YGGY??JYY55?~Y5YYYYYJ?~7!!!!!!JJJJJJJJJJYYJJ?!?J??YP5JJ?^~JJJ?JJ7~!~:...........
............. ^JJ7!^7Y5PP5YJ????YP555JJJY7!!^!JJJJJJJJJJJJYYYPPP55YYYYYYYJJJ77JJ?JY7!!~^............
..............:!?J?!JJ??JYPGGPP5YYY5J??J7:::^YYYYYYYYYYYYYYYYYJJJJJJ7!?JJ7!^~~^:!J!:::..............
............... .^~!?JJJ?77?5GGPPP5J777?^::^Y55YYYYYYY5YYYYYJJ???7~^~!~~^^::~!^^J7~~~~^:............
................. .. :~7???7!7YPPPY!!!7~~~~J55YYJJJJJJ??7!!~~!!7!!?7^~:::~!^:^!^~!!~~^:.............
...................... .:~777!~?777!!7~!!~?YJ??77!!!!~~~~~~~~777777!^~^::~5Y^:^!^...................
......................... .:~7?J?!~^~~^^^:::~????777!!!~~^^^:.:...:~^^~^^:!?~::~~:..................
..............................?YJ?7!^:::...:777!~^::....... ......:~7~^~~~^^^^^~^...................
...............................^7??!~!~~^::........................:!77!!!!!!!!^....................
...............................  :^^^:.:.............................^~!7?77!^:.....................
.................................... ................................ ..............................
....................................................................................................
""")
time.sleep(5)
print("Теперь тебе надо сбежать  от семьи драконов")
time.sleep(2)
print("Перед тобой 4 двери . и Пять жизней")
plaing = True
while plaing:
    door = int(input("Выбери дверь от 1 до 4: "))
    if door == doortrue: 
        print('Поздрвляю ты угадал ')
        print("Смотри!!! Здесь есть сундук!")
        print("Открыть сундук?")
        sunduk1 = input()
        if sunduk1 == "Да" or sunduk1 == "да" or sunduk1 == "y":
            print("Ой тут пароль...")
            time.sleep(2)
            print(f"Подсказка: это {num1} Умножить на {num2}")
            pas1 = int(input("Введи ответ: "))
            pass1 = num1*num2
            print(num1*num2)
            if pas1 == pass1:
                print("Молодец ты нашел золотой меч драконов и золотое яблоко")
                health = health + 3
                sword = True
                print (f"Твое здоровье увиличилось :{health}")
            print("Вот и золотые ворота")
            time.sleep(2)
            print("О нет!!!")
            time.sleep(2)
            dragons = health+1
            print(f"Перед тобой {dragons} драконов")
            dragons_war = dragons-1
            health = health-dragons_war+1
            print(f"ты убил {dragons_war} драконов . и У тебя осталось {health} Жижней. Тебе придстоит убить главного дракона чтобы выжить и сохранить сокровища!")
            if sword == True:
                print("Ты убил дракона своим золотым мечём!")
                sword = False
                time.sleep(2)
                gift = money * 100000000
                print(f"У тебя на руках {gift}$")
                print("Обыскать пещеру?")
                time.sleep(2)
                part = input("Да or Нет")
                if part == "Да" or part == "y" or part == "Да":
                    plays = 3
                    while plays:
                        plays = plays - 1
                        num1 = random.randint(1,10)
                        num2 = random.randint(1,10)
                        summm = num1*num2
                        print("Тебе нужно подобрать пароли")
                        time.sleep(2)
                        print(f"Сколько будет если {num1} Умножить на {num2}?")
                        time.sleep(2)
                        summmuser = input("Ответ: ")
                        if plays == 0:
                            plays = False
                    if summmuser == summm:
                        gift = money*money*2
                        print(f"Теперь у тебя на руках {gift}$")
                        print("и ты выиграл  игру!!!!")
                        plaing = False
                plaing = False
            elif sword == False:
                print("Учи таблицу умножений!!!")
                health = -1
    else:
        health = health - 1
        print(f'Увы ты не угадал У тебя осталось: {health} Жижней')
    if health == 0: 
        print("ты проиграл")
        plaing = False