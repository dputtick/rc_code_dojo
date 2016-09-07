import cProfile
from time import time
from itertools import count
from functools import reduce


def timer(func):
    def wrapper():
        start = time()
        result = func()
        print(time() - start)
        return result
    return wrapper


def count_factors(n):
    count = 0
    step = 2 if n % 2 else 1
    for i in range(1, int(n**0.5), step):
        if n % i == 0:
            count += 2
    return count


def count_factors_reduce(n):
    step = 2 if n % 2 else 1
    return reduce(lambda x, y: x + 2, 
            (i for i in range(1, int(n**0.5), step) if n % i == 0), 0)


def make_triangle_numbers():
    current_triangle = 0
    ints = count(1, 1)
    while True:
        current_int = next(ints)
        current_triangle += current_int
        yield current_triangle


@timer
def get_factors():
    triangles = make_triangle_numbers()
    while True:
        current_triangle = next(triangles)
        num_factors = count_factors(current_triangle)
        if num_factors >= 500:
            return current_triangle


if __name__ == '__main__':
    cProfile.run('get_factors()', sort='tottime')
    print(get_factors())
