import cProfile
from operator import itemgetter

cache = {1: 1}


def next_number(n):
    if n % 2 == 0:
        return n // 2
    elif n % 2 == 1:
        return 3 * n + 1
        

def check_number(n):
    length = 0
    current_number = n
    while current_number not in cache and n > 1:
        current_number = next_number(current_number)
        length += 1
    length += cache[current_number]
    cache[n] = length
    return length


def main():
    for n in range(1, 1000000):
        check_number(n)
    return max(cache.items(), key=itemgetter(1))[0]


if __name__ == '__main__':
    cProfile.run('main()', sort='tottime')
    print(main())


'''
         6226264 function calls in 6.953 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   999999    3.872    0.000    6.422    0.000 august_9.py:14(check_number)
  5226259    2.550    0.000    2.550    0.000 august_9.py:7(next_number)
        1    0.348    0.348    6.953    6.953 august_9.py:25(main)
        1    0.183    0.183    0.183    0.183 {built-in method builtins.max}
        1    0.000    0.000    6.953    6.953 {built-in method builtins.exec}
        1    0.000    0.000    6.953    6.953 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}

'''