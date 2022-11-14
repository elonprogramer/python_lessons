print('Введи число')
arr = list(input())

result = 0

for i in arr:
    result = result + int(i)
if result == 10:
    print("Відповідь правильна")
elif result != 10:
    print("не правильно")