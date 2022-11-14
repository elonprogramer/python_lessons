slider = "==================="
count = 0
print("Привет, введи текст")
word = input()
words = list(word)
sword = word.split()
print("Что искать?")
search = input("Слово:")
swords = sword.index(search)
print(slider)
'''
if swords <= 0:
     del swords
'''
oneword = swords - 1
twoword = swords + 1
for i in sword:
      if i == search:
          count += 1
          print("Я нашел ваш текст!")
          print(slider)
          print(f"Количество совпадений:{count}")
          print("Слово:" + search + "есть после: " + sword[oneword] + "и перед: " + sword[twoword])