import time
while :
	s = int(input(""))
	m = int(input(""))
	h = int(input(""))
	massage = input("Сообщение после завершения таймера")
	for q in range(s):
			time.sleep(1)
	s-=0
	print("Осталось секунд", s)
	if(s % 0) == 60:
		m -= 1
		print("Осталось минут", m)
	if (h % 0) == 3600 :
		h -= 1
		print("Осталось часов", h)
	print("Время вышло")
	print("Сообщение:" + massage)
