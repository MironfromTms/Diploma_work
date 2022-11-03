# list_1 = [2, 5, 7, 10]
# list_2 = [3, 8, 4, 9]
# to_find = 56
#
# can_continue = True
# for x in list_1:
#     for y in list_2:
#         result = x * y
#         print(x, y, result)
#         if result == to_find:
#             print('Found!!!')
#             can_continue = False
#             break
#     if not can_continue:
#         break


# TODO провести рефакторинг кода
def found_the_number(first_list, second_list, number):
    for i_num in first_list:
        for j_num in second_list:
            if i_num * j_num != number:
                yield i_num, j_num, i_num * j_num
            else:
                print('The number has found!')
                return


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
user_number = 56

for i_number in found_the_number(list_1, list_2, user_number):
    print(i_number)

