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
