# def calculating_math_func(data):
#     result = 1
#     for index in range(1, data + 1):
#         result *= index
#     result /= data ** 3
#     result = result ** 10
#     return result


def calculating_math_func(data, user_dict=dict()):
    result = 1
    if data in user_dict:
        result = user_dict[data]
    for i in range(1, data + 1):
        result *= i
        user_dict[i] = result
    result /= data ** 3
    result = result ** 10
    print(user_dict)
    return result


print(calculating_math_func(5))
print(calculating_math_func(10))
print(calculating_math_func(15))
print(calculating_math_func(3))
print(calculating_math_func(7))

