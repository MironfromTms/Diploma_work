# TODO здесь писать код
def my_list(*args):
    answer = list()
    for elem in args:
        if not isinstance(elem, list):
            answer.append(elem)
        else:
            result = my_list(*elem)
            answer.extend(result)
    return answer


numbers_1 = ([[1, 2, [3]], [1], 3])
numbers_3 = [1, 2, 3, 4, 5]
print(sum(my_list(numbers_1)))
print(sum(my_list(numbers_3)))

