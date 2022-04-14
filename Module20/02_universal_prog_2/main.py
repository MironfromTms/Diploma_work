# TODO здесь писать код
def is_prime(number):
    if number > 1:
        for i in range(2, (number // 2) + 1):
            if number % i == 0:
                return False
        return True


def crypto(string):
    answer = list()
    for j_index, j_sym in enumerate(string):
        if is_prime(j_index):
            answer.append(j_sym)
    return answer


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))
