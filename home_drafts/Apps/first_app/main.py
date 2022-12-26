file = open('index.txt', 'r')
data = file.read()
datas = str(data)
math = list(datas)

print(data)
print(math)
file.close()