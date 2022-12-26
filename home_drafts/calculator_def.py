funk_text = ["Добавлять", "Отнимать"]
def hello(name):
    f = funk_text
    my_funk = f"Я умею {f[0]} и {f[1]}"
    result = f"Привет {name}, {my_funk}"
    print(result)
def start():
    hello(neme_input)

def minus(num1, num2):
    print(f"Если {num1} отнять {num2} будет: ")
    result = num1 + num2
    print(result)

def plus(num1, num2):
    print(f"Если {num1} добавить {num2} будет: ")
    result = num1 - num2
    print(result)



neme_input = input("Как вас зовут?: ")
start()
user_funk = f"Какую функцыю надо сделать? "
print(user_funk)
print(f"{funk_text[0]} или {funk_text[1]}")
funk_input = input(funk_text)

if funk_input == funk_text[0]:
    print("Введи первое число:")
    num1 = int(input())
    print("Введи второе число:")
    num2 = int(input())
    plus(num1, num2)
elif funk_input == funk_text[1]:
    print("Введи первое число:")
    num1 = int(input())
    print("Введи второе число:")
    num2 = int(input())
    minus(num1, num2)