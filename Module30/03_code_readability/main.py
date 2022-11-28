print(list(filter(lambda x: all(map(lambda y: x % y != 0, range(2, x))), range(2, 1001))))

nums_list = []
for i in range(2, 1001):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        nums_list.append(i)
print(nums_list)
