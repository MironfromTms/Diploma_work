# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# a.extend(b)
# a.remove(5)
# a.extend(c)
# print('Результат работы программы:')
# print('Кол-во цифр 5 при первом объединении:', a.count(5))
# print('Кол-во цифр 3 при втором объединении:', a.count(3))
# print('Итоговый список: ', a)


# a = []
# for i in range(160, 177, 2):
#     a.append(i)
# print('Первый класс: ', a)
# b = []
# for i in range(162, 180, 3):
#     b.append(i)
# print('Второй класс: ', b)
# a.extend(b)
# a.sort()
# print('Отсортированный список объединенного класса: ', a)

# shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
#         ['педаль', 100], ['седло', 1500], ['рама', 12000],
#         ['обод', 2000], ['шатун', 200], ['седло', 2700]]
#
# detail = input('Название детали: ')
# count = 0
# summ = 0
# for i in shop:
#     for j in i:
#         if j == detail:
#             count += 1
#             summ += i[1]
# print('Кол-во деталей -', count)
# print('Общая стоимость -', summ)

# guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
#
# while True:
#
#     print('Сейчас на вечеринке', len(guests), 'человек: ', guests)
#     answer = input('Гость пришёл или ушёл? ')
#     if answer == 'Пора спать' or answer == 'пора спать':
#         print('Вечеринка закончилась, все легли спать.')
#         break
#     if answer == 'пришёл' or answer == 'пришел':
#         name_1 = input('Имя гостя: ')
#         guests.append(name_1)
#         if len(guests) < 7:
#             print('Привет, ', name_1, '!')
#         else:
#             print('Прости,', name_1, ', но мест нет.')
#             guests.remove(name_1)
#     if answer == 'ушёл' or answer == 'ушел':
#         name_2 = input('Имя гостя: ')
#         if name_2 in guests:
#             guests.remove(name_2)
#             print('Пока,', name_2, '!')

#
# violator_songs = [
#     ['World in My Eyes', 4.86],
#     ['Sweetest Perfection', 4.43],
#     ['Personal Jesus', 4.56],
#     ['Halo', 4.9],
#     ['Waiting for the Night', 6.07],
#     ['Enjoy the Silence', 4.20],
#     ['Policy of Truth', 4.76],
#     ['Blue Dress', 4.29],
#     ['Clean', 5.83]]
#
#
# count = int(input('Сколько песен выбрать? '))
# i = 0
# total = 0
# while count > 0:
#     count -= 1
#     i += 1
#     print('Название', i, 'песни: ', end=' ')
#     song = input()
#     for n in violator_songs:
#         for m in n:
#             if m == song:
#                 index = violator_songs.index(n)
#                 total += violator_songs[index][1]
# print('Общее время звучания песен: ', total)

# while True:
#     contacts = {}
#     for i in range(1000):
#         print('Текущие контакты на телефоне:', contacts)
#         print()
#         name = input('Введите имя: ')
#         if name in contacts:
#             print('Ошибка, имя уже есть в списке контактов.')
#             continue
#         phone_number = input('Введите номер телефона: ')
#         contacts[name] = phone_number


# small_storage = {
#     'гвозди': 5000,
#     'шурупы': 3040,
#     'саморезы': 2000
# }
# big_storage = {
#     'доски': 1000,
#     'балки': 150,
#     'рейки': 600
# }
# big_storage.update(small_storage)
# print(big_storage)
#
# goods = input('Введите название товара: ')
# if goods in big_storage:
#     print(big_storage.get(goods))
# else:
#     print('Такого товара нет в списке')

# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'grapefruit': 300.40,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }

# summ = 0
# for i in incomes.values():
#     summ += i
# print('Общий доход за год составил: ', summ)
# min_value = min(incomes.values())
# sorted_values = sorted(incomes.values())
# print('Самый маленький доход у ', min(incomes, key=incomes.get), '. Он составляет ', min_value)
# incomes.pop(min(incomes, key=incomes.get))
# print('Итоговый словарь: ', incomes)
#
# players_dict = {
#     1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
#     2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
#     3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
#     4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
#     5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
#     6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
#     7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
#     8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
# }
#
# team_member = [
#     player['name']
#     for player in players_dict.values()
#     if player['team'] == 'C' and player['status'] == 'Travel'
# ]
#
# print(team_member)
#
# family_member = {
#     "name": "Jane",
#     "surname": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "name": "Alice",
#             "age": 6
#         },
#         {
#             "name": "Bob",
#             "age": 8
#         }
#     ]
# }
# for i in family_member.keys():
#     print(i, '-', family_member.get(i))
# print(family_member['children'][1].get('name'))

# phrase = input('Введите строку: ')
# punctuation = set(".,;:!?")
# counter = 0
# for i in phrase:
#     if i in punctuation:
#         counter += 1
# print('Количество знаков пунктуации: ', counter)


# from random import randint
# nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
# nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]
# nums_1_set = set(nums_1)
# nums_2_set = set(nums_2)
# print('1-е множество: ', nums_1_set)
# print('2-е множество: ', nums_2_set)
# print('Минимальный элемент 1-го множества: ', min(nums_1_set))
# print('Минимальный элемент 2-го множества: ', min(nums_2_set))
# nums_1_set.remove(min(nums_1_set))
# nums_2_set.remove(min(nums_2_set))
# nums_1_set.add(randint(100, 200))
# nums_2_set.add(randint(100, 200))
# print('Случайное число для 1-го множества: ', max(nums_1_set))
# print('Случайное число для 2-го множества: ', max(nums_2_set))
# print('Объединение множеств: ', nums_1_set | nums_2_set)
# print('Пересечение множеств: ', nums_1_set & nums_2_set)
# print('Элементы, входящие в nums_2, но не входящие в nums_1: ', nums_2_set - nums_1_set)


# string = input('Введите строку:')
# string_set = set()
# for i in string:
#     if '0' <= i <= '9':
#         string_set.add(i)
# string_list = list(string_set)
# string_list.sort()
# answer = ''.join(string_list)
# print('Различные цифры строки: ', answer)

# tuple_1_list = []
# for _ in range(10):
#     tuple_1_list.append(randint(0, 5))
# tuple_2_list = []
# for _ in range(10):
#     tuple_2_list.append(randint(-5, 0))
# tuple_1 = tuple(tuple_1_list)
# print(tuple_1)
# tuple_2 = tuple(tuple_2_list)
# print(tuple_2)
# tuple_3 = tuple_1 + tuple_2
# print(tuple_3)
# print(tuple_3.count(0))

# import math
#
#
# def side_and_fool(raduis, hight):
#     side = 2 * math.pi * raduis * hight
#     full = side + 2 * math.pi * raduis ** 2
#     print('Площадь боковой поверхности -', round(side, 2))
#     print('Полная площадь -', (round(full, 2)))
#     return side, full
#
#
# radius = 100
# hight = 10
#
# side_and_fool(radius, hight)


import random

#
# def change(nums):
#     index = random.randint(0, 4)
#     value = random.randint(100, 1000)
#     nums[index] = value
#     return nums, value
#
#
# my_nums = 1, 2, 3, 4, 5
# my_nums_list = list(my_nums)
# new_nums_1, rand_val_1 = change(my_nums_list)
# print(new_nums_1, rand_val_1)
# new_nums_1_list = list(new_nums_1)
# new_nums_2, rand_val_2 = change(new_nums_1_list)
# rand_val_sum = rand_val_1 + rand_val_2
# print(new_nums_2, rand_val_sum)

#
# number_of_records = int(input('Сколько записей вносится в протокол? '))
# print('Записи (результат и имя):')
# score_dict = dict()
# for i_record in range(1, number_of_records + 1):
#     print(i_record, 'запись:', end='')
#     player_score = input('')
#     player_score_list = player_score.split()
#     if player_score_list[1] not in score_dict.keys():
#         score_dict[player_score_list[1]] = player_score_list[0]
#     else:
#         for j_name, j_score in score_dict.items():
#             if j_name == player_score_list[1]:
#                 score_dict[j_name] = int(j_score) + int(player_score_list[0])
#
# if len(score_dict.keys()) < 3:
#     print('Не достаточное количество игроков. Соревнования не действительны! ')
#
# sorted_values = sorted(score_dict.values())
# sorted_score_dict = dict()
# for i in sorted_values:
#     for i_key in score_dict.keys():
#         if score_dict[i_key] == i:
#             sorted_score_dict[i_key] = score_dict[i_key]
# print(sorted_score_dict)
#
# print('Итоги соревнований:')
# for i_place in range(3):
#     print(i_place + 1, "место:", end='')

# def factorial(num):
#     if num == 1:
#         return 1
#     fac_n_minus_1 = factorial(num-1)
#     return num * fac_n_minus_1
#
#
# num_fact = factorial(5)
# print(num_fact)

# def power(a, n):
#     if n == 0:
#         return 1
#     answer = a * power(a, n - 1)
#     return answer
#
#
# float_num = float(input('Введите вещественное число: '))
# int_num = int(input('Введите степень числа: '))
# print(float_num, '**', int_num, '=', power(float_num, int_num))

# import simple_draw as sd
#
# sd.resolution = (1200, 600)
#
# point = sd.get_point(300, 300)
# radius = 50
# for _ in range(3):
#     radius += 5
#     sd.circle(center_position=point, radius=radius, color=random_color(), width=2)
# sd.pause()

# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
#
#
# def find_key(struct, key):
#     if key in struct:
#         return struct[key]
#
#     for sub_struct in struct.values():
#         if isinstance(sub_struct, dict):
#             result = find_key(sub_struct, key)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
#
# user_key = input('Искомый ключ: ')
# value = find_key(site, user_key)
# if value:
#     print(value)
# else:
#     print('Такого ключа в структуре сайта нет.')

import random
#
#
# def change_dict(dct):
#     num = random.randint(1, 100)
#     for i_key, i_value in dct.items():
#         if isinstance(i_value, list):
#             i_value.append(num)
#         if isinstance(i_value, dict):
#             i_value[num] = i_key
#         if isinstance(i_value, set):
#             i_value.add(num)


# nums_list = [1, 2, 3]
# some_dict = {1: 'text', 2: 'another text'}
# uniq_nums = {1, 2, 3}
#
# common_dict = {1: nums_list.copy(), 2: some_dict.copy(), 3: uniq_nums.copy(), 4: (10, 20, 30)}
#
# change_dict(common_dict)
# print(common_dict)
# print(nums_list, some_dict, uniq_nums)
#
# phrase = input('Введите данные: ')
# print('Тип данных:', type(phrase))
# print('Id объекта:', id(phrase))

import os

# abs_path = os.path.abspath('new_folder')
# print(abs_path)
# abs_path_join = os.path.abspath(os.path.join('..', 'new_folder'))
# print(abs_path_join)
# abs_path_one = os.path.abspath(('/new_folder'))
# print(abs_path_one)
# abs_path_sep = os.path.abspath(os.path.join(os.path.sep, 'new_folder'))
# print(abs_path_sep)

# def print_dirs(project):
#     print('\nСодержимое директории', project)
#     if os.path.exists(project):
#         for i_elem in os.listdir(project):
#             path = os.path.join(project, i_elem)
#             print('     ', path)
#     else:
#         print('Каталога нет!')
#
#
# projets_list = ['Prod', 'PycharmProjects', 'workspace']
# for i_project in projets_list:
#     path_to_project = os.path.abspath(os.path.join('..', '..', i_project))
#     print_dirs(path_to_project)

# rel_path = os.path.join("access", "admin.bat")
# abs_path = os.path.abspath(rel_path)
# print("Абсолютный путь до файла:", abs_path)
# print("Относительный путь до файла:", rel_path)

# print('Содержимое каталога', os.path.abspath(''))
# for path in os.listdir('..'):
#     print(os.path.abspath(path))
#
#
# print("Корень диска:", os.path.abspath('.').split("\\")[0])


# def find_file(cur_path, file_name):
#     print('Переходим', cur_path)
#
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         print('    Смотрим', path)
#         if file_name == i_elem:
#             return path
#         if os.path.isdir(path):
#             print('Это директория')
#             result = find_file(path, file_name)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
#
# file_path = find_file(os.path.abspath
#                       (os.path.join('Module14'))
#                       , 'main.py')
#
# if file_path:
#     print(file_path)
# else:
#     print('Govno')

# path_to = input("Путь: ")
#
# if os.path.isdir(path_to):
#     print("Это папка!")
# elif os.path.isfile(path_to):
#     print("Это файл!")
#     print("Размер файла:", os.path.getsize(path_to), "байт")
# else:
#     print("Указанного пути не существует")


#
# def find_file(cur_path, file_name):
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         if file_name == i_elem:
#             print(os.path.abspath(path))
#         elif os.path.isdir(path):
#             result = find_file(path, file_name)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
#
# find_file('..',  'main.py')

# os.renames(r"C:\folder\first\second",r"C:\catalog\one\two")

# print(os.path.abspath(os.path.join('huy')))

print(os.listdir())
path_to_first = os.path.join('task', 'group_1.txt')
path_to_second = os.path.join('task', 'Additional_info', 'group_2.txt')

file = open(path_to_first, 'r', encoding='utf8')
file_2 = open(path_to_second, 'r', encoding='utf8')

summa = 0
diff = 0
compose = 1

for i_line in file:
    info = i_line.split()
    if info:
        summa += int(info[2])
        diff -= int(info[2])

for i_line in file_2:
    info = i_line.split()
    if info:
        compose *= int(info[2])

file.close()
file_2.close()

print(summa)
print(diff)
print(compose)
