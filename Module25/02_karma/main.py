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


class Human:
    def __init__(self, karma=0):
        self.karma = karma

    def one_day(self):
        if random.randint(1, 10) == 10:
            raise
        else:
            self.karma += random.randint(1, 7)


errors_list = [KillError.__name__, DrunkError.__name__, CarCrashError.__name__, GluttonyError.__name__,
               DepressionError.__name__]
day = 0
human = Human(0)
with open('carma.log', 'a', encoding='utf8') as carma_file:
    while human.karma < 500:
        day += 1
        try:
            human.one_day()
        except:
            carma_file.write(f'At day number {day} the misdemeanor was - {random.choice(errors_list)}\n')

print('You are in nirvana now!')
