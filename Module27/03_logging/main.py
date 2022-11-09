import functools
from collections.abc import Callable
from datetime import datetime


def logging(func: Callable) -> Callable:
    """Decorator which logging code work"""

    @functools.wraps(func)
    def wrapped_funk(*args, **kwargs):
        try:
            print(f'\nWe are calling {func.__name__}\t'
                  f'positional arguments {args}\t'
                  f'callable arguments {kwargs}')
            print('Function has documentation:\n'
                  , func.__doc__)
            result = func(*args, **kwargs)
            return result
        except Exception as error:
            error = f'At {datetime.now()} in function {func.__name__} was exception - {error}'
            with open('function_errors.log', 'a', encoding='utf8') as file:
                file.write(error)
            print(error)

    return wrapped_funk


@logging
def zero_div():
    """Zero division error"""
    x = 1 / 0


zero_div()
