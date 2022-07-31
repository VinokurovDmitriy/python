from datetime import datetime
from time import perf_counter


def timer():
    start = perf_counter()

    def inner():
        return perf_counter() - start

    return inner


def add(a, b):
    return a + b


def counter(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'{func.__name__}call {count}')
        return func(*args, **kwargs)

    return inner


def decorator(func):
    def inner():
        print('start decorator')
        func()
        print('end decorator')
    inner.__name__ = say.__name__
    inner.__doc__ = say.__doc__

    return inner


@decorator
def say():
    """
    function say hi
    :return:
    """
    print('hi')

print(say.__name__)
say()
