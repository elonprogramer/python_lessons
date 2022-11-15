count = 0
print("Привіт, введи текст")
word = input()
sword = word.split()
print("Що шукати?")
search = input("Слово:")
swords = sword.index(search)
for i in sword:
     if i == search:
         count += 1
         print("Я знайшов ваш текст!")
         print(f"Кількість збігів:{count}")
         print(f"Слово: {search} знайдено у реченні:{word}")