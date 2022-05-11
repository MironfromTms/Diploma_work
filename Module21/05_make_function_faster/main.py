# def calculating_math_func(data):
#     result = 1
#     for index in range(1, data + 1):
#         result *= index
#     result /= data ** 3
#     result = result ** 10
#     return result


def calculating_math_func(data, user_dict=dict()):
    result = 1
    for i in range(1, data + 1):
        result *= i
        user_dict[i] = result
        print(user_dict)
    result /= data ** 3
    result = result ** 10
    return result


print(calculating_math_func(5))
print(calculating_math_func(10))
print(calculating_math_func(15))
print(calculating_math_func(3))

