import time
while 10:
	print("Привет")
	time.sleep(1)
	print("Введи первое число")
	first_num = int(input())
	print("Введи второе число")
	second_num = int(input())
	print("Введи знак")
	funk = input("плюс минус умножить подилить степень:")
	if funk == "плюс":
		result = first_num + second_num
		print(f"ответ {first_num}+{second_num}: {result}")
	elif funk == "минус":
		result = first_num - second_num
		print(f"ответ {first_num}-{second_num}: {result}")
	elif funk == "умножить":
		result = first_num * second_num
		print(f"ответ {first_num}*{second_num}: {result}")
	elif funk == "подилить":
		result = first_num / second_num
		print(f"ответ {first_num}/{second_num}: {result}")
	elif funk == "степень":
		result = first_num ** second_num
		print(f"ответ {first_num}**{second_num}: {result}")