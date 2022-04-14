# TODO здесь писать код
def tpl_sort(user_tuple):
    user_list = list(user_tuple)
    sorted_user_list = sorted(user_list)
    sorted_tuple = tuple(sorted_user_list)
    for i in sorted_user_list:
        if int(i) != i:
            return user_tuple
    return sorted_tuple


my_tuple = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(my_tuple))
