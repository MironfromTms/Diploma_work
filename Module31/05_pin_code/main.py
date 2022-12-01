import itertools

pin_code = itertools.product(range(10), repeat=4)
print('Any possible PIN codes:')
for number in pin_code:
    print(*number)