import functools
from collections.abc import Callable


def debug(func: Callable) -> Callable:
    """Decorator which shows name of decorating function,
     its args and kwargs and return its meaning"""

    @functools.wraps(func)
    def wrapped_funk(*args, **kwargs):
        print(f'\nWe are calling function - "{func.__name__}"\t'
              f'positional arguments {args}\t'
              f'callable arguments {kwargs}')
        result = func(*args, **kwargs)
        print(f'Function "{func.__name__}" returned : "{result}"')
        print(result)
        return result

    return wrapped_funk


@debug
def greeting(name, age=None):
    if age:
        return f"Wow, {name}! You are {age} years old , you grow up so fast!"
    else:
        return f"Hi, {name}!"


greeting("Tom")
greeting("Mike", age=55)
greeting(name="Kate", age=16)
