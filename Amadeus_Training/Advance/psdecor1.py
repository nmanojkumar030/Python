""" decorator"""
from time import perf_counter


def to_json(func):
    def wrapper_to_json(*args):
        from json import dumps
        return dumps(func(*args))

    return wrapper_to_json


def timer(func):
    def wrapper_timer(*args, **kwargs):
        start_time = perf_counter()
        value = func(*args)
        end_time = perf_counter()
        print("{}{} took {}".format(func.__name__, args, end_time - start_time))

        return value

    return wrapper_timer


@timer
def compute(n):
    for item in range(100 * n):
        temp = [hex(item) for item in range(1000)]

    return temp


print(compute(5))


@to_json
@timer
def square_n_cube(value):
    return dict(result=(value ** 2, value ** 3))


print(square_n_cube(5))  # to_json(square_n_cube)
