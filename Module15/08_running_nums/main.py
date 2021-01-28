step = int(input('Сдвиг: '))
list = [1, 2, 3, 4, 5]
new_list = []
lenght = len(list)
print('Изначальный список: ', list)
for i in range(lenght, 0, -1):
    if i == lenght - step:
        break
    new_list.append(i)
new_list.reverse()
for j in range(lenght-step):
    new_list.append(list[j])
print(new_list)