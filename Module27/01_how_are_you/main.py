# TODO здесь писать код
from typing import Callable


def how_are_you(func):
    def wrapped_func(*args, **kwargs):
        are_you_ok = input('How are you?')
        print('I am not OK! Alright, where is are function!')
        value = func(*args, **kwargs)
        return
    return wrapped_func


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()
