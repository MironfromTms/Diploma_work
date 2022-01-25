# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for i in b:
#     a.append(i)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1
# print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)

# TODO переписать программу
a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

for i in b:
    a.append(i)
count_fives = 0

for i in a:
    if i == 5:
        count_fives += 1
print('Кол-во цифр 5 при первом объединении:', count_fives)

for i in a:
    if i == 5:
        a.remove(i)

for i in c:
    a.append(i)
count_threes = 0
for i in a:
    if i == 3:
        count_threes += 1
print('Кол-во цифр 3 при втором объединении:', count_threes)
print('Итоговый список: ', a)
