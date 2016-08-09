import cProfile
from operator import itemgetter

cache = {1: 1}


def next_number(n):
    if n % 2 == 0:
        return n // 2
    elif n % 2 == 1:
        return 3 * n + 1


def check_number(n):
    current_list = []
    current_number = n
    while current_number not in cache and n > 1:
        current_list.append(current_number)
        current_number = next_number(current_number)
    length = cache[current_number]
    for index, number in enumerate(reversed(current_list)):
        cache[number] = length + (index + 1)
    return length


def main():
    for n in range(1, 1000000):
        check_number(n)
    return max(cache.items(), key=itemgetter(1))[0]


if __name__ == '__main__':
    cProfile.run('main()', sort='tottime')
    print(main())


'''
         5337225 function calls in 7.399 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   999999    4.482    0.000    6.141    0.000 august_9_2.py:14(check_number)
  2168610    1.260    0.000    1.260    0.000 august_9_2.py:7(next_number)
        1    0.638    0.638    7.399    7.399 august_9_2.py:26(main)
        1    0.620    0.620    0.620    0.620 {built-in method builtins.max}
  2168610    0.399    0.000    0.399    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    7.399    7.399 {built-in method builtins.exec}
        1    0.000    0.000    7.399    7.399 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}

    '''

