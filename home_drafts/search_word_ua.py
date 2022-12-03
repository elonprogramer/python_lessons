slider = "==================="
count = 0
print("Привіт, введи текст")
word = input()
words = list(word)
sword = word.split()
print("Що шукати?")
search = input("Слово:")
swords = sword.index(search)
print(slider)
oneword = swords - 1
twoword = swords + 1
for i in sword:
     if i == search:
         count += 1
         print("Я знайшов ваш текст!")
         print(slider)
         print(f"Кількість збігів:{count}")
         print("Слово:" + search + "є після: " + sword[oneword] + "та перед: " + sword[twoword])


     elif i != search:
         print(f"Знайдено {count} . в даному тексті немає: " + search)
         print(i)