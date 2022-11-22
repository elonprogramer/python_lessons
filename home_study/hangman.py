import random
hangman_pics = [''' 
+---+
    |
    |
    |
   ===''',
'''
+---+
O   |
    |
    |
   ===''',
'''
+---+
0   |
|   |
    |
   ===''',
'''
 +---+
 0   |
/|   |
     |
    ===''',
'''
 +---+
 0   |
/|\  |
     |
    ===''','''
 +---+
 0   |
/|\  |
/    |
    ===''',
'''
 +---+
 0   |
/|\  |
/ \  |
    ===''']
words = '''аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея
индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось ля-
гушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон
попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'''.split()



def getrandomword(wordlist):
	# Эта функция возвращает случайную строку из переданного списка.
	wordindex = random.randint(0, len(wordlist) - 1)
	return wordlist[wordindex]

def displayboard(missedletters, correctletters, secretword):
	print(hangman_pics[len(missedletters)])
	print()

	print('ошибочные буквы:', end=' ')
	for letter in missedletters:
		print(letter, end=' ')
	print()

	blanks = '_' * len(secretword)

	for i in range(len(secretword)):  # заменяет пропуски отгаданными буквами
		if secretword[i] in correctletters:
			blanks = blanks[:i] + secretword[i] + blanks[i+1:]

	for letter in blanks:  # Показывает секретное слово с пробелами между буквами
		print(letter, end=' ')
	print()


def getguess(alreadyguessed):
	while True:
		print('Введите букву.')
		guess = input()
		guess = guess.lower()
		if len(guess) != 1:
			print('Пожалуйста введите одну букву.')
		elif guess in alreadyguessed:
			print('Вы уже назвали эту букву. назовите другую.')
		elif guess not in 'абвгдеежзийклмнопрстуфхцчшщъыьэюя':
			print('Пожалуйста, введите БУКВУ.')
		else:
			return guess


def playagain():
	print("Хотите сыграть еще? (да или нет)")
	return input().lower().startswith('д')

print('В И С Е Л И Ц А')
missedletters = ''
correctletters = ''
secretword = getrandomword(words)
print(secretword)
gameisdone = False

while True:
	displayboard(missedletters, correctletters, secretword)
	guess = getguess(missedletters + correctletters)

	if guess in secretword:
		correctletters = correctletters + guess
		foundallletters = True
		for i in range(len(secretword)):
			if secretword[i] not in correctletters:
				foundallletters = False
				break
		if foundallletters:
			print('ДА Секретное слово- "' + secretword + '"!Вы угадали!')
			gameisdone = True
	else:
		missedletters = missedletters + guess

		if len(missedletters) == len(hangman_pics) - 1:
			displayboard(missedletters, correctletters, secretword)
			print('Вы исчерпали все попытки!\nНе угадано букв: ' + str(len(missedletters)) + ' и угадано букв: ' + str(len(correctletters)) + '. Было загадано слово "' + secretword + '".')
			gameisdone = True


	if gameisdone:
		if playagain():
			missedletters = ''
			correctletters = ''
			gameisdone = False
			secretword = getrandomword(words)
		else:
			break