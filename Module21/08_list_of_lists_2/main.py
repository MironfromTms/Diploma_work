nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


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


print(my_list(nice_list))
