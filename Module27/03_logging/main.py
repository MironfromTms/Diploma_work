import functools
from collections.abc import Callable


def counter(func: Callable) -> Callable:
    """Decorator which counts how many times
     we called decorating function"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        print(f'Function with name "{func.__name__}" has called {wrapper.count} times.')
        return result

    wrapper.count = 0
    return wrapper


@counter
def test():
    print('Hello')


test()
test()
test()
