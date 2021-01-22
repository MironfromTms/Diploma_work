number = int(input('Введите число: '))
i = 1
while i <= number:
    i = i + 1
    if number % i == 0:
        break
print('Наименьший делитель, отличный от единицы: ', i)
