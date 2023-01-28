import random

max_input = 3

letters = "abcdefghijklmnopqrstuvwxyz"
# letters = list(letters)
# lenlist = len(letters)
letters_choice = ""
while len(letters_choice) == 3: 
    letters_choice = letters_choice + random.choice(letters)

# print(letters_choice)

user_input = input("Введи 3 буквы")

user_input_answer = list(user_input)
user_input_length = len(user_input)

if user_input_length > max_input:
    print("Ты ввел больше букв")
elif user_input_length < max_input:
    print("Ты ввел меньше букв")