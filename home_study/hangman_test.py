import random
words = '''аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея
индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось ля-
гушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон
попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'''.split()

40. def getRandomWord(wordList):
41.# Эта функция возвращает случайную строку из переданного списка.
42.wordIndex = random.randint(0, len(wordList) - 1)
43.return wordList[wordIndex]
44.
45. def displayBoard(missedLetters, correctLetters, secretWord):
46.print(HANGMAN_PICS[len(missedLetters)])
47.print()
48.
49.print('Ошибочные буквы:', end=' ')
50.for letter in missedLetters:
51.
52.
print(letter, end=' ')
print()
53.
54.
blanks = '_' * len(secretWord)
55.
56.
57.
for i in range(len(secretWord)): # заменяет пропуски отгаданными буквами
if secretWord[i] in correctLetters:
58.
blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
59.
60.
61.
62.
for letter in blanks: # Показывает секретное слово с пробелами между буквами
print(letter, end=' ')
print() def getGuess(alreadyGuessed):
# Возвращает букву, введенную игроком. Эта функция проверяет, что игрок ввел только одну букву и ничего больше.
while True:
print('Введите букву.')
guess = input()
guess = guess.lower()
if len(guess) != 1:
print('Пожалуйста, введите одну букву.')
elif guess in alreadyGuessed:
print('Вы уже называли эту букву. Назовите другую.')
elif guess not in 'абвгдеежзийклмнопрстуфхц