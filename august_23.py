from concurrent.futures import ProcessPoolExecutor
import time


# what are various ways I can solve this problem?
    # Computation using lists
    # Computation using generators?
    # Using a mask of some sort?
    # Using numpy operations?
    # Using concurrency/multiprocessing? Including various approache s?
    # Implement different sieves altogether (atkin, sundaram)
    # Alternative ways of checking the rotations of primes

# (all ints <= N) -> primes -> check rotations of each prime -> len of list
# ints -> primes -> if rotations less than N then check if in primes otherwise check prime
# ints -> primes


def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def check_prime(n):
    if is_prime(n):
        return(n)


def main(chunk):  
    nums = range(1, 1000)
    pool = ProcessPoolExecutor()
    count = 0
    returned_iterator = pool.map(is_prime, nums, timeout=None, chunksize=chunk)
    for result in returned_iterator:
        if result:
            count += 1
    return count
    
def reference():
    nums = range(1, 10000)
    count = 0
    results = map(is_prime, nums)
    for result in results:
        if result:
            count += 1
    return count

if __name__ == '__main__':
    for chunk in [1, 2, 4, 8, 16, 32, 64, 128, 256]:
        start = time.time()
        main(chunk)
        print("Chunk:", chunk, "time:", time.time() - start)
    start = time.time()
    reference()
    reftime = time.time() - start
    print("Reference:", reftime)
