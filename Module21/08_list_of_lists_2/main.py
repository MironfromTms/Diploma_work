nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


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


print(my_list(nice_list))
