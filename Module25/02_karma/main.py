import random


class KillError(Exception):
    def __str__(self):
        return 'KillError'


class DrunkError(Exception):
    def __str__(self):
        return 'DrunkError'


class CarCrashError(Exception):
    def __str__(self):
        return 'CarCrashError'


class GluttonyError(Exception):
    def __str__(self):
        return 'GluttonyError'


class DepressionError(Exception):
    def __str__(self):
        return 'DepressionError'


def one_day():
    if random.randint(1, 10) == 10:
        errors_list = [KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()]
        exc = random.choice(errors_list)
        raise exc
    else:
        return random.randint(1, 7)


day = 0
karma = 0
with open('carma.log', 'a', encoding='utf8') as carma_file:
    while karma < 500:
        day += 1
        try:
            karma += one_day()
        except(KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as exc:
            carma_file.write(f'At day number {day} the misdemeanor was - {exc}\n')

print('You are in nirvana now!')
