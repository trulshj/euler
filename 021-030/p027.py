import math
from time import time
start_time = time()


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def consecutive_quadratics(a, b):
    consecutive = 0
    n = 0
    while True:
        quadratic = (math.pow(n, 2) + (a * n) + b)
        if is_prime(quadratic):
            consecutive += 1
            n += 1
        else:
            return consecutive


largest_consecutive = 0
longest_a_b = (0, 0)
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        c = consecutive_quadratics(a, b)
        if c > largest_consecutive:
            largest_consecutive = c
            longest_a_b = (a, b)

print(f"n^2 + {longest_a_b[0]}n + {longest_a_b[1]} gives the longest consecutive chain".center(64))
print(f"with {largest_consecutive} consecutive primes, the product a*b is {longest_a_b[0] * longest_a_b[1]}".center(64))
print(f"Found in {time()-start_time} seconds".center(64))
