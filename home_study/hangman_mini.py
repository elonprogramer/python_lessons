import random
words = '''агу еге'''.split()

wordindex = random.randint(0, len(words) - 1)
tword = words [wordindex]
stword = list(tword)
col = len(stword)

print("Привет, введи букву")
blanks = '_'*len(tword)

game = True
while game:
    sword = input()

    for i in stword:
          if i == sword:
              print("Вы угадали букву!")
