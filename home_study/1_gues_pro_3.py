#Это игра по угадыванию чисел
import random

guassestaken = 0

cheatkey = "john_doe"


number = random.randint(1,20)


print ('Привет! как тебя зовут?')

name = input ()
if name == cheatkey:
  print(int(number)+2)

print ('Что ж ' + name + ', я загадываю число от 1 до 20.')

for guassestaken in range(6):
	print ('Попробуй угадать')
	guess = input ()
	guess = int(guess)
	if guess < number:
		print('Твое число слишком маленькое' )
	elif guess > number:
		print('Твое число слишком большое')
	elif guess == number:
		break
if guess == number:
	guassestaken = str(guassestaken + 1)
	print ('Отлично, ' + name + ' Ты справился за ' + guassestaken + ' попытки!')
elif guess != number:
	number = str(number)
	print('Увы. Я загадал число ' + number + '.')