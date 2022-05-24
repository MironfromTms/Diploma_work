# TODO здесь писать код

def moves(steps, x=1, y=3):
    if steps == 1:
        print(f'Переложит диск {steps} со стержня номер {x} на стержень номер {y}')
    else:
        moves(steps - 1, x, 6 - x - y)
        print(f'Переложит диск {steps} со стержня номер {x} на стержень номер {y}')
        moves(steps - 1, 6 - x - y, y)


disc_number = int(input('Введите количество дисков:'))
moves(disc_number)
