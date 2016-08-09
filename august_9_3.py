import cProfile
from operator import itemgetter

cache = {1: 1}


def next_number(n):
    if n % 2 == 0:
        return n // 2
    elif n % 2 == 1:
        return 3 * n + 1


def collatz_length(n):
    next_num = next_number(n)
    if next_num in cache:
        cache[n] = cache[next_num] + 1
    else:
        cache[n] = collatz_length(next_num) + 1
    return cache[n]


def main():
    for n in range(1, 1000000):
        collatz_length(n)
    return max(cache.items(), key=itemgetter(1))[0]

if __name__ == '__main__':
    cProfile.run('main()', sort='tottime')
    print(main())



'''
         5472500 function calls (3736252 primitive calls) in 6.443 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
2736247/999999    3.778    0.000    5.296    0.000 august_9_3.py:14(collatz_length)
  2736247    1.518    0.000    1.518    0.000 august_9_3.py:7(next_number)
        1    0.755    0.755    0.755    0.755 {built-in method builtins.max}
        1    0.391    0.391    6.443    6.443 august_9_3.py:23(main)
        1    0.000    0.000    6.443    6.443 {built-in method builtins.exec}
        1    0.000    0.000    6.443    6.443 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''