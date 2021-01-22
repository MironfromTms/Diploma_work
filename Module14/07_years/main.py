number_1 = int(input('Введите первый год: '))
number_2 = int(input('Введите второй год: '))
print('Годы от', number_1, 'до', number_2, 'с тремя одинаковыми цифрами: ')
for number in range(number_1, number_2 + 1):
    a = number % 10
    b = ((number - a) % 100) / 10
    c = (number - b * 10 - a) % 1000 / 100
    d = (number - c * 100 - b * 10 - a) / 1000
    if a == b == c:
        print(number)
    elif a == c == d:
        print(number)
    elif b == c == d:
        print(number)
    elif a == b == d:
        print(number)