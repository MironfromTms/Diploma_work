# TODO здесь писать код
def shift(string):
    new_str = string[-1]
    for i in range(len(string)-1):
        new_str += string[i]
    return new_str


first_str = input('Первая строка: ')
second_str = input('Вторая строка: ')
if len(first_str) == len(second_str):
    step = 0
    for i in range(len(first_str)):
        if first_str == second_str:
            print(f' Первая строка получается из второй со сдвигом {step}.')
            break
        else:
            second_str = shift(second_str)
            step += 1
    if len(second_str) == step:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
