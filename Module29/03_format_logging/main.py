import functools
from datetime import datetime
import time
from typing import Callable


def timer(cls, func, date_format) -> Callable:
    @functools.wraps(cls)
    def wrapped(*args, **kwargs):
        wrapped_format = date_format
        for sym in wrapped_format:
            if sym.isalpha():
                wrapped_format = wrapped_format.replace(sym, '%' + sym)
        print(
            f"Now starting '{cls.__name__}.{func.__name__}'."
            f" Current date and starting time: {datetime.now ().strftime(wrapped_format)}")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Ending '{cls.__name__}.{func.__name__}', time of work = {round(end - start, 3)} sec.")
        return result

    return wrapped


def log_methods(date_format):
    @functools.wraps(date_format)
    def decorate(cls):
        for i_method in dir(cls):
            if not i_method.startswith('__'):
                current_method = getattr(cls, i_method)
                decorated_method = timer(cls, current_method, date_format)
                setattr(cls, i_method, decorated_method)
        return cls

    return decorate


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Heir test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
