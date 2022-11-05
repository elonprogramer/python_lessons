import time
print("Привет")
print("Сколько действий нужно обчислить?")
coll = input()
while int(coll):
	time.sleep(1)
	print("Введи первое число")
	first_num = int(input())
	print("Введи второе число")
	second_num = int(input())
	print("Введи знак")
	funk = input("плюс минус умножить поделить степень:")
	if funk == "плюс":
		result = first_num + second_num
		print(f"ответ {first_num}+{second_num}: {result}")
	elif funk == "минус":
		result = first_num - second_num
		print(f"ответ {first_num}-{second_num}: {result}")
	elif funk == "умножить":
		result = first_num * second_num
		print(f"ответ {first_num}*{second_num}: {result}")
	elif funk == "поделить":
		result = first_num / second_num
		print(f"ответ {first_num}/{second_num}: {result}")
	elif funk == "степень":
		result = first_num ** second_num
		print(f"ответ {first_num}**{second_num}: {result}")