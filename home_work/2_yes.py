import time
import random
number_attemps = 0
print ('Как тебя зовут')
#name = input()
time.sleep(1)
print('Попробуй угадать')
namber = random.randint(1,20)
#print('Что ж,' + name + ', я загадываю число от 1 до 20.')
for number_attemps in range(6):
	print('Попробуй угадать')
	print('Попытка ' + str(number_attemps))