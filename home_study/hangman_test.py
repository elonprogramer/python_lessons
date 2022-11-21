import random
hangman_pics = 5
words = '''аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея
индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось ля-
гушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон
попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'''.split()


wordindex = random.randint(0, len(words) )
secretword = words [wordindex]

print()
print('обычные буквы:', end='')
print()
blanks = '_' * len (secretword)
print(blanks)
print(secretword)
for i in range (len(secretword)):
	if secretword[i] in blanks:
		blanks = blanks[:i] + secretword[i] + blanks[i+1:]

	for letter in blanks:
		print(letter, end='')
	print()


	
while True:
	print('Введите букву.')
	guess = input()
	guess = guess.lower()
	if len(guess) !=1:
		print('Пожалуста введите одну букву.')
	elif guess in blanks:
		print('Вы уже назвали эту букву. назовити другую.')
	elif guess not in 'абвгдеежзийклмнопрстуфхцчшщъыьэюя':
			print('Пожалуйста, введите БУКВУ.')
	else:
		print("Ошыбка")