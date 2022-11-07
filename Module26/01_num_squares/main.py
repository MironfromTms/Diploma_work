# TODO здесь писать код
class SquareOfNumberIter:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < self.n:
            self.i += 1
            return self.i ** 2
        else:
            raise StopIteration


def square_of_numbers_gen(user_num):
    for i in range(1, user_num + 1):
        yield i ** 2


number = int(input('Input your number: '))

square_of_numbers = (num ** 2 for num in range(1, number + 1))
for i_num in square_of_numbers:
    print(i_num, end=' ')

print()

square_of_numbers_iter = SquareOfNumberIter(number)
for j_num in square_of_numbers_iter:
    print(j_num, end=' ')

print()

for k_num in square_of_numbers_gen(number):
    print(k_num, end=' ')
