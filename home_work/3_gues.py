#Это игра по угадыванию чисел
import random

guassestaken = 0

print ('Привет! как тебя зовут?')

name = input ()

number = random.randint(1,20)

print ('Что ж' + name + ', я загадываю число от 1 до 20.')

for guassestaken in range(6):
	print ('Попробуй угадать')
	guess = input ()
	guess = int(guess)
	if guess < number:
		print('Твое число слишком маленькое')
	if guess > number:
		print('Твое число слишком большое')
	if guess == number:
		break
if guess == number:
	guassestaken = str(guassestaken + 1)
	print ('Отлично,' + name + 'Ты справился за' + guassestaken + 'попыткы!')
if guess != number:
	number = str(number)
	print('Увы. Я загадал число' + number + '.')