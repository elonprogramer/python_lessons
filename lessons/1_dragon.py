import random
import time

def  displayintro():
	print('''Вы находитесь в землях, заселенных драконами.
 Перед собой вы видите две пещеры. В одной из них — дружелюбный дракон,
 который готов поделиться с вами своими сокровищами. 
 Во второй — жадный и голодный дракон, который мигом вас съест''')
	print()

def choosecave():
	cave = ''
	while cave != '1' and cave != '2':
		print('В какую пещеру вы войдете? (нажмите клавишу 1 или 2)')
		cave = input('1 or 2:')

	return cave

def chackcave(choosecave):
	print('вы приближаетесь к пещере...')
	time.sleep(2)
	print('Ее темнота заставляет вас дрожать от страха...')
	time.sleep(2)
	print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
	print()
	time.sleep(2)

	friendlycave = random.randint(1,2)

	if choosecave == str(friendlycave):
		print('... делится с вами своими сокровищами')
	else:
		print('моминтально вас сьедает!')

playagain = 'да'
while playagain == 'да' or playagain == 'д' or playagain == 'y' or playagain == 'yes':
	displayintro()
	cavenumber = choosecave()
	chackcave(cavenumber)

	print('Попытаете удачу еще раз?')
	playagain = input('да or нет:')
