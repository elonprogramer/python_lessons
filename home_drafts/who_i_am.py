#Игра кто я?
import time
#как меня зовут?
print("Во что играем? ")
time.sleep(2)
print("Узнать имя - n узнать фамилию - s")
catch = input ()

if catch == "n":
	print("Какая ваша фамилия?")
surname = input()
if surname == "Галацан":
	name = "Юрий"
	print(f"ваше имя: {name}")


#Какая моя фамилия
if catch == "s":
	print("Как вас зовут?")
name = input()
if name == "Юрий":
	surname = "Галацан"
	print(f"ваша фамилия: {surname}")