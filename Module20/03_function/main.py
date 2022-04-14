# TODO здесь писать код
def slicer(user_tuple, number):
    user_list = list(user_tuple)
    counter = 0
    for i_index, i_number in enumerate(user_list):
        if number == i_number:
            counter += 1
    if counter == 0:
        print(user_tuple)
    elif counter == 1:
        new_list_1 = user_list[user_list.index(number):]
        print(tuple(new_list_1))
    else:
        new_list_2 = user_list[user_list.index(number):-(user_list.index(number))]
        print(tuple(new_list_2))


slicer((1, 3, 4, 2, 5, 6, 7, 2, 8, 9, 10), 2)
