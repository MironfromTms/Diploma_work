import random

carma = 0
day = 1


def one_day(number):
    if random.randint(1, 10) == 10:
        with open('carma.log', 'a', encoding='utf8') as carma_file:
            misdemeanor = random.choices(['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError',
                                          'DepressionError'])
            carma_file.write(f'At day number {number} the misdemeanor was - {misdemeanor}\n')


while carma < 500:
    one_day(day)
    day += 1
    carma += random.randint(1, 7)
print('You are in nirvana now!')
