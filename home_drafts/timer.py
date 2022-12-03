import time
print ('Введи количество секунд')
sec = int(input())
time.sleep(2)
slider = "======================="
print(slider)
time.sleep(2)
print(slider)
one = 1
for i in range(one, sec):
	print(i)
