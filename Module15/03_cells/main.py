cells = int(input('Кол-во клеток: '))
cells_list = []
for i in range(cells):
    print('Эффективность', i + 1, 'клетки: ', end='')
    a = int(input())
    cells_list.append(a)
print('Неподходящие значения: ', end='')
for i in range(cells):
    if cells_list[i] < i:
        print(cells_list[i], end=' ')