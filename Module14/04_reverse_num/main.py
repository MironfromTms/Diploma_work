def firstPart(number):
    mantisa = ''
    mantisa_new = ''
    for i in number:
        if i == '.':
            break
        mantisa += i
    for j in reversed(mantisa):
        mantisa_new += j
    return mantisa_new


def secoundPart(number):
    level = ''
    for j in reversed(number):
        if j == '.':
            break
        level += j
    return level


number_1 = input('Введите первое число: ')
firstPart_1 = firstPart(number_1)
secoundPart_1 = secoundPart(number_1)
number_2 = input('Введите второе число: ')
firstPart_2 = firstPart(number_2)
secoundPart_2 = secoundPart(number_2)
firstNumber = firstPart_1 + '.' + secoundPart_1
secoundNumber = firstPart_2 + '.' + secoundPart_2
print('Первое число наоборот: ', firstNumber)
print('Второе число наоборот: ', secoundNumber)
print('Сумма: ', float(firstNumber) + float(secoundNumber))

