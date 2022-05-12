# TODO здесь писать код
def my_list(*args):
    answer = list()
    for elem in args:
        for sub_elem in elem:
            if not isinstance(sub_elem, list):
                answer.append(sub_elem)
            else:
                result = my_list(sub_elem)
                answer.extend(result)
    return answer


numbers_1 = ([[1, 2, [3]], [1], 3])
numbers_2 = (1, 2, 3, 4, 5)
print(sum(my_list(numbers_1)))
print(sum(my_list(numbers_2)))
