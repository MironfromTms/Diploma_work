import random


def first_function(x, y):
    x += random.randint(0, 5)
    y += random.randint(0, 10)
    return x / y


def second_function(x, y):
    x -= random.randint(0, 5)
    y -= random.randint(0, 10)
    return y / x


# try:
#     file = open('coordinates.txt', 'r')
#     for line in file:
#         nums_list = line.split()
#         res1 = f(int(nums_list[0]), int(nums_list[1]))
#         try:
#             res2 = f2(int(nums_list[0]), int(nums_list[1]))
#             try:
#                 number = random.randint(0, 100)
#                 file_2 = open('result.txt', 'w')
#                 my_list = sorted([res1, res2, number])
#                 file_2.write(' '.join(my_list))
#             except Exception:
#                 print("Что-то пошло не так : ")
#         except Exception:
#             print("Что-то пошло не так со второй функцией")
#         finally:
#             file.close()
#             file_2.close()
# except Exception:
#     print("Что-то пошло не так с первой функцией")


with open('coordinates.txt', 'r') as file:
    for line in file:
        nums_list = line.split()
        try:
            first_result = first_function(int(nums_list[0]), int(nums_list[1]))
        except ZeroDivisionError:
            print('В первой функции произошло деление на ноль!')
        try:
            second_result = second_function(int(nums_list[0]), int(nums_list[1]))
        except ZeroDivisionError:
            print('Вo второй функции произошло деление на ноль!')
number = random.randint(1, 100)
with open('result.txt', 'w') as result_file:
    result_list = sorted([first_result, second_result, number])
    for i_elem in result_list:
        result_file.write(str(i_elem) + ' ')