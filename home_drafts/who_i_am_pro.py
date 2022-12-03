#Игра кто я?
import time
#как меня зовут?
print("Что помним? ")
time.sleep(2)
print("Имя - n фамилию - s год рождения - y")
catch = input ()

#Юрий

#Моё имя
if catch == "n":
	print("Какая ваша фамилия?")
surname = input()
if surname == "Галацан":
	name = "Юрий"
	year = "2004"
	print(f"ваше имя: {name}, ваша фамилия: {surname}, Год рождения: {year}")


#Какая моя фамилия
if catch == "s":
	print("Как вас зовут?")
name = input()
if name == "Юрий":
	surname = "Галацан"
	year = "2004"
	print(f"ваше имя: {name}, ваша фамилия: {surname}, Год рождения: {year}")

"""
#Влад

#Год рождения
if catch == "y":
	print("Когда вы родились?")
year = input()
if year == "2011":
	name = "Влад"
	surname = "Галацан"
	print(f"ваше имя: {name}, ваша фамилия: {surname}, Год рождения: {year}")


#Моё имя
if catch == "n":
	print("Какая ваша фамилия?")
surname = input()
if surname == "Галацан":
	name = "Влад"
	year = "2011"
	print(f"ваше имя: {name}, ваша фамилия: {surname}, Год рождения: {year}")


#Какая моя фамилия
if catch == "s":
	print("Как вас зовут?")
name = input()
if name == "Влад":
	surname = "Галацан"
	year = "2011"
	print(f"ваше имя: {name}, ваша фамилия: {surname}, Год рождения: {year}")

#Год рождения
if catch == "y":
	print("Когда вы родились?")
year = input()
if year == "2011":
	name = "Влад"
	surname = "Галацан"
	print(f"ваше имя: {name}, ваша фамилия: {surname}, Год рождения: {year}")
"""