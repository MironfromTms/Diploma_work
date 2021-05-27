number = int(input('Введите целое число: '))
list = []
for i in range(1, number+1):
    if i % 2 != 0:
        list.append(i)
print(list)

