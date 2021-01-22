
def numSumm(number):
    summ_num = 0
    number = str(number)
    for i in number:
        a = int(i)
        summ_num += a
    return summ_num


def numCounter(number):
    n = 1
    while number // 10 > 0:
        n += 1
        number /= 10
    return n


number = int(input('Введите число: '))
summ = numSumm(number)
counter = numCounter(number)
print('Сумма чисел: ', summ)
print('Кол-во цифр в числе: ', counter)
print('Разность суммы и кол-ва цифр: ', summ - counter)
