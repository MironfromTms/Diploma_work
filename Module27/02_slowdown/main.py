# TODO здесь писать код
import time


def time_track(func):
    def wrapped_func(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Function worked {elapsed} second(s)')
        return result

    return wrapped_func


def slow_down(func):
    def wrapped_func(*args, **kwargs):
        started_at = time.time()
        time.sleep(3)
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Function has slowed down and now worked {elapsed} second(s)')
        return result

    return wrapped_func


@time_track
def hard_func():
    return [x ** 2 ** x for x in range(22)]


hard_func()


@slow_down
def not_so_hard_func():
    return [x ** 2 * x for x in range(22)]


not_so_hard_func()
