import random
hangman_pics = [''' 
+---+
    |
    |
    |
   ===''','''
+---+
   |
    |
    |
   ===''','''
+---+
0   |
|   |
    |
   ===''','''
 +---+
 0   |
/|   |
     |
    ===''','''
 +---+
 0   |
/|\  |
     |
    ===''','''
 +---+
 0   |
/|\  |
/    |
    ===''','''
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
	return wordlist [wordindex]

def displayboard(missedlettrs, correctlettres, secretWord):
	print(hangman_pics[len (missedlettrs)])
	print()

	print('обычные буквы:', end='')
	for letter in missedlettrs:
		print(letter, end='')
	print()

	blanks = '_' * len (secretword)

	for i in range (len(secretword)):
		if secretword[i] in correctlettres:
			blanks = blanks[:i] + secretword[i] + blanks[i+1:]

	for letter in blanks:
		print(letter, end='')
	print()

def getguess (alreadyguessed):
	
	while True:
		print('Введите букву.')
		guess = input()
		guess = guess.lower()
		if len(guess) !=1:
			print('Пожалуста введите одну букву.')
		elif guess in alreadyguessed:
			print('Вы уже назвали эту букву. назовити другую.')
		elif guess not in 'абвгдеежзийклмнопрстуфхцчшщъыьэюя':
				print('Пожалуйста, введите БУКВУ.')
		else:
			return guess

def playagain():
	print("Хотите сыграть еще? (да или нет)")
	return input().lower().startswith('д')



print('В И С Е Л И Ц А')
missedlettrs = ''
correctlettres = ''
secretword = getrandomword(words)
gameisdone = False

while True:
	displayboard(missedlettrs, correctlettres, secretword)


	guess = getguess(missedlettrs + correctlettres)

	if guess in secretword:
		correctlettres = correctlettres + guess


		foundallletters = True
		for i in range(len(secretword)):
			if secretword[i] not in correctlettres:
				foundallletters = False
				break
			if foundallletters:
				print('ДА Секретное слово- "' + secretword + '"!Вы угадали!')
				gameisdone = True
			else:
				missedlettrs = missedlettrs + getguess


				if len(missedlettrs) == len(hangman_pics) - 1:
					displayboard(missedlettrs,correctlettres,secretword)
print('Вы исчерпали все попытки!\nНе угадано букв: ' + str(len(missedletters)) + ' и угадано букв: ' + str(len(correctlettres)) + '. Было загадано слово "' + secretword + '".')
gameisdone = True


if gameisdone:
		if playagain():
				missedlettrs = ''
				correctlettres = ''
				gameisdone = False
				secretword = getrandomword(words)
