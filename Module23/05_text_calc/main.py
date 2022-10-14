# TODO здесь писать код
with open('calc.txt', 'r') as file:
    result = []
    for i_line in file:
        try:
            result.append(eval(i_line))
        except:
            user_answer = input('Обнаружена ошибка в строке :{} Хотите исправить?'.format(i_line)).lower()
            if user_answer == 'yes' or user_answer == 'да':
                i_line = input('Введите исправленную строку:')
                result.append(eval(i_line))
    print('Сумма результатов: ', round(sum(result), 2))
