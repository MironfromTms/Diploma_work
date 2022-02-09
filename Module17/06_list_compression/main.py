# TODO здесь писать код
import random

nums = int(input('Кол-во чисел в списке: '))
nums_list = [random.randint(0, 2) for _ in range(nums)]
print('Список до сжатия: ', nums_list)

no_zero_nums_list = [x for x in nums_list if x != 0]
print('Список после сжатия: ', no_zero_nums_list)