# TODO здесь писать код
original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 0
new_list = list()
for i_number in range(5):
    new_list.append(tuple(original_list[n:n+2]))
    n += 2
print(new_list)

